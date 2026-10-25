from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        """
        Initialize MongoDB connection.
        """

        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
    'mongodb://%s:%s@%s:%d/?authSource=aac'
    % (USER, PASS, HOST, PORT)
    )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        """
        Insert a document into the collection.

        Args:
            data (dict): Document to insert

        Returns:
            bool: True if successful, otherwise False
        """
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            else:
                return False

        except Exception as e:
            print("Create Error:", e)
            return False

    # Read method to implement the R in CRUD
    def read(self, query):
        """
        Read matching documents from the collection.

        Args:
            query (dict): Search criteria

        Returns:
            list: Matching documents
        """
        try:
            cursor = self.collection.find(query)
            return list(cursor)

        except Exception as e:
            print("Read Error:", e)
            return []

    # Update method to implement the U in CRUD
    def update(self, query, update_data):
        """
        Update matching documents in the collection.

        Args:
            query (dict): Search criteria
            update_data (dict): New values

        Returns:
            int: Number of documents modified
        """
        try:
            result = self.collection.update_many(
                query,
                {"$set": update_data}
            )

            return result.modified_count

        except Exception as e:
            print("Update Error:", e)
            return 0

    # Delete method to implement the D in CRUD
    def delete(self, query):
        """
        Delete matching documents from the collection.

        Args:
            query (dict): Search criteria

        Returns:
            int: Number of documents removed
        """
        try:
            result = self.collection.delete_many(query)

            return result.deleted_count

        except Exception as e:
            print("Delete Error:", e)
            return 0