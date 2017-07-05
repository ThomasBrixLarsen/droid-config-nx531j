#!/bin/sh

if [ ! -f /system/etc/boot_fixup_sailfish ];then
  mount -o rw,remount,barrier=1 /system
  touch /system/etc/boot_fixup_sailfish
  mv /audio_policy.conf /system/etc
  mount -o ro,remount,barrier=1 /system
fi
