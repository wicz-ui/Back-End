import * as fs from "node:fs";
import { fileURLToPath } from "node:url";

const arquivo = new URL("./saida.txt", import.meta.url);
const conteudo = "Olá! Arquivo criado pelo Node usando fs.\n";

fs.writeFileSync(arquivo, conteudo, "utf8");
console.log("Arquivo criado em:", fileURLToPath(arquivo));
