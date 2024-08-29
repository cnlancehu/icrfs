#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::ptr;
use windows::Win32::UI::Shell::{SHChangeNotify, SHCNE_ASSOCCHANGED, SHCNF_IDLIST};

fn main() {
    unsafe {
        SHChangeNotify(
            SHCNE_ASSOCCHANGED,
            SHCNF_IDLIST,
            Some(ptr::null_mut()),
            Some(ptr::null_mut()),
        );
    };
}
