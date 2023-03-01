db.auth("root", "toor");

db = db.getSiblingDB("dbOkan");

db.createUser({
  user: "adminOkan",
  pwd: "adminOkan",
  roles: [
    {
      role: "readWrite",
      db: "dbOkan",
    },
  ],
});
