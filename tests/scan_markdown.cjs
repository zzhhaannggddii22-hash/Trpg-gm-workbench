const fs = require("node:fs");
const { lexer, walkTokens } = require("marked");

const documents = JSON.parse(fs.readFileSync(0, "utf8"));
const results = {};
for (const [path, source] of Object.entries(documents)) {
  const tokens = lexer(source, { gfm: true });
  const links = [];
  const headings = [];
  walkTokens(tokens, (token) => {
    if (token.type === "link" || token.type === "image") {
      links.push([token.href, token.raw]);
    }
    if (token.type === "heading") {
      headings.push(token.text);
    }
  });
  results[path] = { links, headings };
}
process.stdout.write(JSON.stringify(results));
