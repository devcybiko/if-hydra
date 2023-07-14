#/bin/bash
set -e

for i in `find . -name "*.js"`; do
    echo
    echo $i ...
    $i
done

for i in `find . -name "*.py"`; do
    echo
    echo $i ...
    $i
done

echo
echo "All tests passed."