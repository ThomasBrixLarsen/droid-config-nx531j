# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device nx531j
%define vendor nubia
%define vendor_pretty Nubia
%define device_pretty Nubia Z11
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.75
# We assume most devices will
%define have_modem 1

# Community HW adaptations need this
%define community_adaptation 1

Provides: ofono-configs
Provides: sensord-configs

%include droid-configs-device/droid-configs.inc
