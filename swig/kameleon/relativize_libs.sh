#!/bin/bash -e

# https://unix.stackexchange.com/a/289896

#[ -n "$1" ] || set -- a.out
mkdir -p ./lib/ #<copy the libraries here

#use ldd to resolve the libs and use `patchelf --print-needed to
# filter out "magic" libs kernel-interfacing libs such as
# linux-vdso.so, ld-linux-x86-65.so or libpthread which you probably
# should not relativize anyway

#join <(ldd "$1" |awk '{if(substr($3,0,1)=="/") print $1,$3}' |sort) <(patchelf --print-needed "$1" |sort) |cut -d\  -f2 | xargs -d '\n' -I{} cp --copy-contents {} ./lib

# Correction ($3,0,1) -> ($3,0,2)
join <(ldd "$1" |awk '{if(substr($3,0,2)=="/") print $1,$3}' |sort) <(patchelf --print-needed "$1" |sort) |cut -d\  -f2 | xargs -d '\n' -I{} cp --copy-contents {} ./lib 

#make the relative lib paths override the system lib path
# Original:
#patchelf --set-rpath "\$ORIGIN/." "$1"
# Modification:
cp "$1" lib/
cd lib/; patchelf --set-rpath "\$ORIGIN/." "$1"
