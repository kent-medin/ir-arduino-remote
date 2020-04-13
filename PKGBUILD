pkgname=ir-arduino-remote
pkgver=0.0.1
pkgrel=1
pkgdesc="Ir arduino remote"
url="https://github.com/kent-medin/ir-arduino-remote"
arch=(x86_64)
license=(MIT)

depends=("python3" "python-pyserial" "python-evdev" "libevdev")

source=(
  "git+https://github.com/kent-medin/ir-arduino-remote.git"  
)
sha256sums=('SKIP')

package() {
  install -Dm644 $srcdir/ir-arduino-remote/service/ir-arduino-remote.service $pkgdir/lib/systemd/system/ir-arduino-remote.service
  install -Dm644 $srcdir/ir-arduino-remote/service/keys.json $pkgdir/etc/ir-arduino-remote/keys.json
  install -Dm744 $srcdir/ir-arduino-remote/service/ir_remote_service.py $pkgdir/usr/bin/ir_remote_service.py
}