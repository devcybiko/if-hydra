py=$1
js=$2
if [[ "$py" == "" || "$js" == "" ]]; then
	echo "py-to-js.sh <a.py> <a.js>"
	exit 0
fi
export UNGREEDY
cat "$py" | \
sed -E 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/env node\nconst process = require("process");/' |\
sed -E 's/def ([^:]*).*/}\n\nfunction \1 {/' | \
sed -E 's/ and / \&\& /g' | \
sed -E 's/ or / || /g' | \
sed -E 's/( +)if ([^:]+): *$/\1~ (\2) {/' | \
sed -E 's/( +)if ([^:]+):(.*)$/\1if (\2)\3;/' | \
sed -E 's/~/if/' | \
sed -E 's/( +)elif ([^:]*): *$/\1} else if (\2) {/' | \
sed -E 's/( +)elif ([^:]*):(.*)$/\1else if (\2)\3;/' | \
sed -E 's/( +)else: *$/\1} else {/' | \
sed -E 's/( +)else:(.*)$/\1else \2;/' | \
sed -E 's/( +)print(\([^)]*\))/\1console.log\2/' | \
sed -E 's/({[a-zA-Z0-9]+})/$\1/g' |\
sed -E 's/f"([^"]*)"/`\1`/' |\
# sed -E 's/[:] *$/ {/' | \
# sed -E 's/[:](.*) (#+.*)$/ {\1; \2/' | \
# sed -E 's/[:](.*)$/ {\1;/' | \
sed -E 's/"""/ \/\//' | \
sed -E 's/#[^!]#*/\/\//g' | \
sed -E 's/==/===/g' | \
sed -E 's/exit\(\)/process.exit();/' | \
sed -E 's/^main\(\)/}\nmain();\n/' | \
cat > "$js"

chmod a+x "$js"