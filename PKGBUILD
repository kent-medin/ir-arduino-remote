pkgname=ir-arduino-remote
pkgver=0.0.1
pkgrel=1
pkgdesc="Ir arduino remote"
url="https://github.com/kent-medin/ir-arduino-remote"
arch=(x86_64)
license=(MIT)

depends=("python3", "python-pyserial", "python-evdev", "libevdev")

source=(
  "git+https://github.com/kent-medin/ir-arduino-remote.git"  
)
md5sums=('SKIP' 'SKIP')



package() {
  cd "service"

  install -Dm644 ir-arduino-remote.service /lib/systemd/system/ir-arduino-remote.service
  intsall -Dm644 keys.json /etc/ir-arduino-remote/keys.json
  install -Dm744 ir_remote_service.py /usr/bin/ir_remote_service.py
}