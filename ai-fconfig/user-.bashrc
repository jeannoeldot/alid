#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

### PS1 CONFIG
# ORIGINAL
#PS1='[\u@\h \W]\$ '
# Mon PS1
COLOR_OFF='\[\e[m\]'
VERT="\[\e[0;32m\]"
BLEU="\[\e[0;34m\]"
BLANC="\[\e[0;37m\]"
BOLDVERT="\[\e[1;32m\]"
BOLDBLEU="\[\e[1;34m\]"
BOLDCYAN="\[\e[1;36m\]"
BOLDBLANC="\[\e[1;37m\]"
#
#PS1="$BOLDVERT\u $BOLDBLEU\W $BOLDVERT\$$BOLDBLANC "
#
#PS1="$BOLDVERT╔\u$COLOR_OFF $BOLDBLEU\w$COLOR_OFF\n$BOLDVERT╚═> \$$COLOR_OFF$BOLDBLANC "
#
PS1="$BOLDVERT┌\u$COLOR_OFF $BOLDBLEU( \w )$COLOR_OFF\n$BOLDVERT└─> \$$COLOR_OFF$BOLDBLANC "


### BASH OPTIONS
shopt -s cdspell                 # Correct cd typos
#shopt -s checkwinsize            # Update windows size on command
shopt -s histappend              # Append History instead of overwriting file
shopt -s cmdhist                 # Bash attempts to save all lines of a multiple-line command in the same history entry
shopt -s extglob                 # Extended pattern
shopt -s no_empty_cmd_completion # No empty completion
### COMPLETION
if [[ -f /etc/bash_completion ]]; then
    . /etc/bash_completion
fi

### BASH HISTORY
export HISTSIZE=10000           # bash history will save N commands
export HISTFILESIZE=${HISTSIZE} # bash will remember N commands
export HISTCONTROL="ignoreboth:erasedups"   # ingore duplicates and spaces
export HISTIGNORE='&:ls:ll:la:cd:exit:clear:history'

### EXPORTS

### ALIAS
alias ls='ls --color=auto'
alias grep='grep --color=auto'
#
alias maj='su -c "pacman -Syu" -'

