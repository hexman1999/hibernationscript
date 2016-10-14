# Maintainer: Muhammad Ashraf <mohamedraesa@gmail.com>

pkgname=simple-hibernation-script
pkgver=1.0
pkgrel=1
pkgdesc="Python script for hibernating the pc after a period of sleep using interactive terminal"
arch=('any')
url="https://github.com/mohamedraesa/hibernationscript/blob/master/HibernateScript.py"
license=('gpl')
depends=('python3', 'pm-utils', 'systemd', 'libsystemd')

build() {
git clone https://github.com/mohamedraesa/hibernationscript/ hiberscript
#cd hibernationscript-Master
#mkdir usr
#cd usr
#mkdir bin
#mv ../HibernationScript.py bin/hibernation-script
}

package() {
  install -D -m755 $srcdir/hiberscript/HibernateScript.py "$pkgdir/usr/bin/simple-hibernation-script"
  install -D -m644 $srcdir/hiberscript/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

