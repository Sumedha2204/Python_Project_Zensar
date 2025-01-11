import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from urllib.parse import urlparse, parse_qs

# MySQL database connection
db_config = {
    'user': 'root',
    'password': 'root@123',
    'host': 'localhost',
    'database': 'farm_produce_management'
}

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Handler for HTTP requests
class RequestHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self, content_type='application/json'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
    
    def _send_response(self, data):
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        # Parsing the URL to check for specific resource
        parsed_path = urlparse(self.path)
        resource = parsed_path.path.strip('/')
        
        # Handle requests for specific resources
        if resource == 'produce':
            self.get_produce()
        elif resource == 'inventory':
            self.get_inventory()
        elif resource == 'sales':
            self.get_sales()
        elif resource == 'customers':
            self.get_customers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Resource not found")
    
    def get_produce(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Produce")
        produce = cursor.fetchall()
        self._set_headers()
        self._send_response(produce)
        cursor.close()
        conn.close()

    def get_inventory(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Inventory")
        inventory = cursor.fetchall()
        self._set_headers()
        self._send_response(inventory)
        cursor.close()
        conn.close()

    def get_sales(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Sales")
        sales = cursor.fetchall()
        self._set_headers()
        self._send_response(sales)
        cursor.close()
        conn.close()

    def get_customers(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Customers")
        customers = cursor.fetchall()
        self._set_headers()
        self._send_response(customers)
        cursor.close()
        conn.close()

    def do_POST(self):
        # Handle POST requests for inserting records
        parsed_path = urlparse(self.path)
        resource = parsed_path.path.strip('/')
        
        if resource == 'produce':
            self.add_produce()
        elif resource == 'sales':
            self.add_sales()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Resource not found")

    def add_produce(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        name = data['Name']
        category = data['Category']
        description = data['Description']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Produce (Name, Category, Description) VALUES (%s, %s, %s)", (name, category, description))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Produce added successfully"})
        cursor.close()
        conn.close()

    def add_sales(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        produce_id = data['ProduceID']
        quantity_sold = data['QuantitySold']
        total_price = data['TotalPrice']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Sales (ProduceID, QuantitySold, TotalPrice) VALUES (%s, %s, %s)", 
                       (produce_id, quantity_sold, total_price))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Sale recorded successfully"})
        cursor.close()
        conn.close()

    def do_PUT(self):
        # Handle PUT requests for updating records
        parsed_path = urlparse(self.path)
        resource = parsed_path.path.strip('/')
        
        if resource == 'produce':
            self.update_produce()
        elif resource == 'inventory':
            self.update_inventory()
        elif resource == 'sales':
            self.update_sales()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Resource not found")
    
    def update_produce(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        produce_id = data['ProduceID']
        name = data['Name']
        category = data['Category']
        description = data['Description']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Produce SET Name=%s, Category=%s, Description=%s WHERE ProduceID=%s", 
                       (name, category, description, produce_id))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Produce updated successfully"})
        cursor.close()
        conn.close()

    def update_inventory(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        inventory_id = data['InventoryID']
        stock_quantity = data['StockQuantity']
        unit_price = data['UnitPrice']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Inventory SET StockQuantity=%s, UnitPrice=%s WHERE InventoryID=%s", 
                       (stock_quantity, unit_price, inventory_id))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Inventory updated successfully"})
        cursor.close()
        conn.close()

    def update_sales(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        sales_id = data['SalesID']
        quantity_sold = data['QuantitySold']
        total_price = data['TotalPrice']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Sales SET QuantitySold=%s, TotalPrice=%s WHERE SalesID=%s", 
                       (quantity_sold, total_price, sales_id))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Sales record updated successfully"})
        cursor.close()
        conn.close()\
        
    def do_DELETE(self):
        # Handle DELETE requests for deleting records
        parsed_path = urlparse(self.path)
        resource = parsed_path.path.strip('/')
        
        if resource == 'produce':
            self.delete_produce()
        elif resource == 'inventory':
            self.delete_inventory()
        elif resource == 'sales':
            self.delete_sales()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Resource not found")
    
    def delete_produce(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        produce_id = query_params.get('ProduceID', [None])[0]
        
        if not produce_id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"ProduceID is required")
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produce WHERE ProduceID=%s", (produce_id,))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Produce deleted successfully"})
        cursor.close()
        conn.close()

    def delete_inventory(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        inventory_id = query_params.get('InventoryID', [None])[0]
        
        if not inventory_id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"InventoryID is required")
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Inventory WHERE InventoryID=%s", (inventory_id,))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Inventory deleted successfully"})
        cursor.close()
        conn.close()

    def delete_sales(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        sales_id = query_params.get('SalesID', [None])[0]
        
        if not sales_id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"SalesID is required")
            return
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Sales WHERE SalesID=%s", (sales_id,))
        conn.commit()
        
        self._set_headers()
        self._send_response({"message": "Sales record deleted successfully"})
        cursor.close()
        conn.close()

# Start the server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run(port=8000)
