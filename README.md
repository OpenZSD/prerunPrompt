<h1 style="color: #006cff; font-size: 50px;"><img style="margin-bottom: -15px;" src="doc_files/logoSolid.png" width="70"/> SOFT DEVELOPMENT </h1>

# Pre-run Prompt
A simple python utility to show a dialog before running command.

## Flags
### -s `<size>`
***"fullscreen"*** for full screen or ***"#x#"*** for a given size.

### -m `<msg>`
Message to show

### -c `<cmd>`
Command to run

### -t '<seconds>'
Seconds before the prompt goes away and runs command

## Building
run `./buildWhl.sh`

## Installing
Run `sudo pip3 install PrerunPrompt-1.0.0-py3-none-any.whl`
<br>
Then in a seperate terminal run `setupPrerunPrompt`