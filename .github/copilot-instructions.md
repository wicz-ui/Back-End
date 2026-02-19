# Copilot Instructions - Back-End Project

## Project Overview
Simple Node.js backend project combining MySQL database connectivity with file system operations. Main entry point is `banco.js` which tests MySQL connections. The `Alfa/` folder contains experimental scripts for learning file I/O patterns.

## Architecture & Key Components

### Database Layer (`banco.js`)
- **Technology**: MySQL2 with promise-based async/await pattern
- **Pattern**: Connects to MySQL using environment variables (DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME)
- **Error Handling**: Errors caught and logged with status code `process.exit(1)`
- **Connection Cleanup**: Always calls `connection.end()` in finally block to prevent hanging connections
- **Configuration**: Uses `dotenv` to load `.env` file with database credentials

### File Operations (`Alfa/` folder)
- **Pattern**: ES6 modules with `import` statements
- **File Writing**: Uses `writeFileSync()` or `appendFileSync()` from `node:fs`
- **Path Resolution**: Uses `import.meta.url` with `fileURLToPath()` for ESM-compatible file paths
- **Output**: Multiple scripts write to `saida.txt`

## Project Conventions

### Module System
- **Type**: ES6 modules (`"type": "module"` in package.json)
- **Import Style**: Use `import` statements, not `require()`
- **Node Built-ins**: Reference as `node:fs`, `node:url`, etc.

### Environment Configuration
- Sensitive credentials stored in `.env` file (not committed)
- Variables accessed via `process.env.VARIABLE_NAME`
- Default values provided where appropriate (e.g., `DB_PORT || 3306`)

### Async Patterns
- `async/await` for promise handling in database operations
- `try/finally` for resource cleanup (database connections)

## Running the Project

```bash
# Install dependencies
npm install

# Execute database test (requires running MySQL with proper .env credentials)
node banco.js

# Execute file operations scripts
node Alfa/index.js
node Alfa/index2.js
```

## Common Debugging Points

1. **MySQL Connection Failures**: Check that MySQL is running and `.env` has correct credentials
2. **Module Import Errors**: Ensure `"type": "module"` is in package.json
3. **Empty Error Messages**: Errors from MySQL driver may have undefined messages - wrap in error handling

## File Structure Reference
- `banco.js` - Main database connection test
- `Alfa/index.js` & `Alfa/index2.js` - File writing operations
- `.env` - Database credentials (never commit)
- `Alfa/saida.txt` - Output file from file I/O operations
