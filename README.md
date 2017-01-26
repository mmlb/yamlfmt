# yamlfmt

A simple opionated yaml formatter that keeps your comments!

`yamlfmt` is just a cli wrapper around the [ruamel.yaml](https://bitbucket.org/ruamel/yaml) python library, which happens to have the unique quality of keeping comments.

### Usage

**Note**:
The formatting used is subject to change without notice.
Once a format seems to stick v1.0 will be tagged and the format will not change.

```sh
❯ yamlfmt -h
usage: yamlfmt [-h] [-w] [file [file ...]]

positional arguments:
  file         file to parse

optional arguments:
  -h, --help   show this help message and exit
  -w, --write  write formatted outpout to (source) file instead of stdout
```

### Examples

Lets see `yamlfmt` in action:

#### Simple example from ruamel.yaml docs
```sh
❯ yamlfmt <<EOF
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
EOF
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
```

#### Travis-CI nodejs example
```sh
❯ yamlfmt <<EOF
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
language: node_js

# test on two node.js versions: 0.6 and 0.8
node_js:
- 0.6
- 0.8

# configure notifications (email, IRC, campfire etc)
# please update this section to your needs!
notifications:
  irc: irc.freenode.org#travis
```

#### Complex example from ruamel.yaml docs
```sh
❯ yamlfmt <<EOF
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
```
