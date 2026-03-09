import mysql from "mysql2/promise";

const db = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "escola",
  database: "sucos_vendas",
});

export default db;