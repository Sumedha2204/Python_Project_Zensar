CREATE TABLE Produce (
    ProduceID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Category VARCHAR(30) NOT NULL,
    Description VARCHAR(200)
);

CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    ContactInfo VARCHAR(100),
    Address VARCHAR(200),
    ProduceID INT NOT NULL,
    FOREIGN KEY (ProduceID) REFERENCES Produce(ProduceID) ON DELETE CASCADE
);

CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    ProduceID INT NOT NULL,
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),
    UnitPrice DECIMAL(10, 2) NOT NULL CHECK (UnitPrice > 0),
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    SupplierID INT,
    FOREIGN KEY (ProduceID) REFERENCES Produce(ProduceID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL
);

CREATE TABLE Sales (
    SalesID INT AUTO_INCREMENT PRIMARY KEY,
    ProduceID INT NOT NULL,
    QuantitySold INT NOT NULL CHECK (QuantitySold > 0),
    TotalPrice DECIMAL(10, 2) NOT NULL, 
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProduceID) REFERENCES Produce(ProduceID) ON DELETE CASCADE
);

CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    ContactInfo VARCHAR(100)
);


INSERT INTO Produce (Name, Category, Description) VALUES 
('Tomatoes', 'Vegetable', 'Fresh red tomatoes'),
('Wheat', 'Grain', 'High-quality wheat grains'),
('Apples', 'Fruit', 'Organic apples from the orchard'),
('Carrots', 'Vegetable', 'Crunchy and fresh carrots'),
('Bananas', 'Fruit', 'Sweet ripe bananas'),
('Rice', 'Grain', 'Long-grain basmati rice'),
('Onions', 'Vegetable', 'Golden onions'),
('Strawberries', 'Fruit', 'Fresh garden strawberries'),
('Corn', 'Grain', 'Sweet corn kernels'),
('Potatoes', 'Vegetable', 'Premium quality potatoes');

INSERT INTO Suppliers (Name, ContactInfo, Address, ProduceID) VALUES
('AgriSupplier Inc.', '1234567890', '123 Farm Lane', 1),
('Farm Supplies Co.', '0987654321', '456 Crop Street', 2),
('Orchard Goods', '1112223334', '789 Orchard Avenue', 3),
('Green Fields Supplies', '2223334445', '321 Green Street', 4),
('Harvest Distributors', '5556667778', '654 Harvest Road', 5);

INSERT INTO Inventory (ProduceID, StockQuantity, UnitPrice, SupplierID) VALUES
(1, 500, 20.50, 1),
(2, 1000, 15.00, 2),
(3, 300, 50.00, 3),
(4, 600, 25.00, 4),
(5, 400, 10.00, 5),
(6, 2000, 12.00, 2),
(7, 800, 18.00, 1),
(8, 350, 30.00, 3),
(9, 700, 22.00, 4),
(10, 1200, 12.50, 5),
(1, 200, 19.00, 1),
(5, 300, 9.50, 5);

INSERT INTO Customers (Name, ContactInfo) VALUES
('Alice Johnson', 'alice.johnson@example.com'),
('Bob Smith', 'bob.smith@example.com'),
('Charlie Brown', 'charlie.brown@example.com'),
('Diana Prince', 'diana.prince@example.com'),
('Ethan Hunt', 'ethan.hunt@example.com'),
('Fiona Carter', 'fiona.carter@example.com');

INSERT INTO Sales (ProduceID, QuantitySold, TotalPrice, SaleDate) VALUES
(1, 20, 410.00, NOW()),
(2, 50, 750.00, NOW() - INTERVAL 1 DAY),
(3, 10, 500.00, NOW() - INTERVAL 2 DAY),
(4, 30, 750.00, NOW() - INTERVAL 3 DAY),
(5, 15, 150.00, NOW() - INTERVAL 4 DAY),
(6, 100, 1200.00, NOW() - INTERVAL 5 DAY),
(7, 25, 450.00, NOW() - INTERVAL 6 DAY),
(8, 12, 360.00, NOW() - INTERVAL 7 DAY),
(9, 40, 880.00, NOW() - INTERVAL 8 DAY),
(10, 50, 625.00, NOW() - INTERVAL 9 DAY);
