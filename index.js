import db from "./db.js";

const [rows, fields] = await db.query("SELECT * FROM notas_fiscais");
console.log(rows, fields);
process.exit(0);
