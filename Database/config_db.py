async def delete_all_messages(self):
await self.col.delete_many(())
mdb = Database(DATABASE_URI, "admin_database")
ndb = Database(DATABASE_ URI, "adnin_ database")
