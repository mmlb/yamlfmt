python -m yamlfmt <<EOF
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
EOF

python -m yamlfmt <<EOF
language: node_js

# test on two node.js versions: 0.6 and 0.8
node_js:
  - 0.6
  - 0.8

# configure notifications (email, IRC, campfire etc)
# please update this section to your needs!
notifications:
  irc: "irc.freenode.org#travis"
EOF

python -m yamlfmt <<EOF
- &CENTER {x: 1, y: 2}
- &LEFT {x: 0, y: 2}
- &BIG {r: 10}
- &SMALL {r: 1}
# All the following maps are equal:
# Explicit keys
- x: 1
  y: 2
  r: 10
  label: center/big
# Merge one map
- <<: *CENTER
  r: 10
  label: center/big
# Merge multiple maps
- <<: [*CENTER, *BIG]
  label: center/big
# Override
- <<: [*BIG, *LEFT, *SMALL]
  x: 1
  label: center/big
EOF

python -m yamlfmt samples/a.yaml
python -m yamlfmt -i 5 samples/b.yaml