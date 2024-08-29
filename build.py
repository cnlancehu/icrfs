import zipfile
import os
import subprocess

app_name = "icrfs"

targets = {
    "x86_64-pc-windows-msvc": "windows-x86_64",
    "i686-pc-windows-msvc": "windows-x86",
    "aarch64-pc-windows-msvc": "windows-aarch64",
    "i586-pc-windows-msvc": "windows-i586",
}

os.environ["RUSTFLAGS"] = "-C target-feature=+crt-static"

os.makedirs("dist", exist_ok=True)

for target, alias in targets.items():
    subprocess.Popen(f"rustup target add {target}", stdout=subprocess.PIPE, text=True, shell=True).wait()
    subprocess.Popen(f"cargo build -r --target {target}", stdout=subprocess.PIPE, text=True, shell=True, env=os.environ).wait()
    with zipfile.ZipFile(os.path.join("dist", f"{app_name}-{alias}.zip"), "w") as zipf:
        app_name_with_extension = f"{app_name}.exe"
        zipf.write(os.path.join("target", target, "release", app_name_with_extension), arcname=app_name_with_extension)
    os_name, arch = alias.split("-")
