##Name: Sumedha Karpe
##College : AVCOE


# Python_Project_Zensar
# Farm Produce Inventory and Sales Management System

## Project Overview
This project implements a RESTful API for managing a farm produce inventory and sales management system. The API is built using Python's `http.server` module and connects to a MySQL database to handle CRUD operations for the following entities:

- Produce
- Inventory
- Sales
- Customers
- Suppliers

The system supports operations such as creating, reading, updating, and deleting records from these entities, ensuring seamless data management.

## Features
- CRUD operations for all entities.
- SQL-backed storage for persistent data.
- Lightweight, Python-native HTTP server without external frameworks like Flask.
- Designed for ease of use and testing with tools like Postman.

---

## Database Schema

### 1. Produce Table
| Column       | Type          | Constraints |
|--------------|---------------|-------------|
| ProduceID    | INT           | PRIMARY KEY, AUTO_INCREMENT |
| Name         | VARCHAR(50)   | NOT NULL    |
| Category     | VARCHAR(30)   | NOT NULL    |
| Description  | VARCHAR(200)  |             |

### 2. Suppliers Table
| Column       | Type          | Constraints |
|--------------|---------------|-------------|
| SupplierID   | INT           | PRIMARY KEY, AUTO_INCREMENT |
| Name         | VARCHAR(50)   | NOT NULL    |
| ContactInfo  | VARCHAR(100)  |             |
| Address      | VARCHAR(200)  |             |
| ProduceID    | INT           | FOREIGN KEY REFERENCES Produce(ProduceID) ON DELETE CASCADE |

### 3. Inventory Table
| Column       | Type          | Constraints |
|--------------|---------------|-------------|
| InventoryID  | INT           | PRIMARY KEY, AUTO_INCREMENT |
| ProduceID    | INT           | FOREIGN KEY REFERENCES Produce(ProduceID) ON DELETE CASCADE |
| StockQuantity| INT           | CHECK (StockQuantity >= 0) |
| UnitPrice    | DECIMAL(10,2) | CHECK (UnitPrice > 0)       |
| LastUpdated  | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |
| SupplierID   | INT           | FOREIGN KEY REFERENCES Suppliers(SupplierID) ON DELETE SET NULL |

### 4. Sales Table
| Column       | Type          | Constraints |
|--------------|---------------|-------------|
| SalesID      | INT           | PRIMARY KEY, AUTO_INCREMENT |
| ProduceID    | INT           | FOREIGN KEY REFERENCES Produce(ProduceID) ON DELETE CASCADE |
| QuantitySold | INT           | CHECK (QuantitySold > 0)    |
| TotalPrice   | DECIMAL(10,2) | NOT NULL                   |
| SaleDate     | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP  |

### 5. Customers Table
| Column       | Type          | Constraints |
|--------------|---------------|-------------|
| CustomerID   | INT           | PRIMARY KEY, AUTO_INCREMENT |
| Name         | VARCHAR(50)   | NOT NULL                   |
| ContactInfo  | VARCHAR(100)  |                            |

---

## API Endpoints

### 1. Produce
**GET** `/produce`  
Fetches all records from the `Produce` table.

**POST** `/produce`  
Creates a new record in the `Produce` table.  
**Request Body:**
```json
{
    "Name": "Tomatoes",
    "Category": "Vegetable",
    "Description": "Fresh red tomatoes"
}
```

**PUT** `/produce`  
Updates an existing record in the `Produce` table.  
**Request Body:**
```json
{
    "ProduceID": 1,
    "Name": "Tomatoes",
    "Category": "Vegetable",
    "Description": "Updated description"
}
```

**DELETE** `/produce?ProduceID=1`  
Deletes a record from the `Produce` table using the `ProduceID` query parameter.

### 2. Inventory
**GET** `/inventory`  
Fetches all records from the `Inventory` table.

**POST** `/inventory`  
Creates a new inventory record.  
**Request Body:**
```json
{
    "ProduceID": 1,
    "StockQuantity": 500,
    "UnitPrice": 20.50,
    "SupplierID": 1
}
```

**PUT** `/inventory`  
Updates an existing inventory record.  
**Request Body:**
```json
{
    "InventoryID": 1,
    "StockQuantity": 600,
    "UnitPrice": 21.00
}
```

**DELETE** `/inventory?InventoryID=1`  
Deletes a record from the `Inventory` table using the `InventoryID` query parameter.

### 3. Sales
**GET** `/sales`  
Fetches all records from the `Sales` table.

**POST** `/sales`  
Records a new sale.  
**Request Body:**
```json
{
    "ProduceID": 1,
    "QuantitySold": 10,
    "TotalPrice": 200.00
}
```

**PUT** `/sales`  
Updates an existing sales record.  
**Request Body:**
```json
{
    "SalesID": 1,
    "QuantitySold": 15,
    "TotalPrice": 300.00
}
```

**DELETE** `/sales?SalesID=1`  
Deletes a record from the `Sales` table using the `SalesID` query parameter.

---

## Testing the API

Use Postman to test the API:

### Testing GET Requests
1. Set the method to `GET`.
2. Use URLs like:
    - `http://localhost:8000/produce`
    - `http://localhost:8000/inventory`

### Testing POST Requests
1. Set the method to `POST`.
2. Provide a valid JSON body (e.g., for `/produce`):
```json
{
    "Name": "Carrots",
    "Category": "Vegetable",
    "Description": "Crunchy and fresh carrots"
}
```

### Testing PUT Requests
1. Set the method to `PUT`.
2. Provide a valid JSON body (e.g., for `/produce`):
```json
{
    "ProduceID": 2,
    "Name": "Wheat",
    "Category": "Grain",
    "Description": "High-quality grains"
}
```

### Testing DELETE Requests
1. Set the method to `DELETE`.
2. Use URLs like:
    - `http://localhost:8000/produce?ProduceID=2`
    - `http://localhost:8000/inventory?InventoryID=3`

---

## Running the Server
To run the server, execute the following command in your terminal:
```bash
python api_server.py
```
The server will start on `http://localhost:8000`.

---

## Dependencies
- Python 3.x
- MySQL Server
- MySQL Connector for Python (`pip install mysql-connector-python`)

---

## Future Enhancements
- Add authentication and authorization.
- Implement pagination for large datasets.
- Enhance error handling.
- Add support for more complex queries (e.g., reports, summaries).

