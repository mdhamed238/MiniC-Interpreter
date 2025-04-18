#! /bin/sh

if [ -f MiniC/Makefile ]; then
    make -C MiniC/ doc && 
    rm -fr public/ && 
    mv MiniC/doc/_build/html/ public/
else
    mkdir public
    cat >public/index.html <<EOF
<html>
<head>
<title>No documentation, yet</title>
</head>
<body>
<h1>No MiniC directory, hence no documentation yet. Come back later.</h1>
</body>
</html>
EOF
fi
