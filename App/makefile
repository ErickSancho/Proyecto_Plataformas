# ICO=$(readlink -e dollar.icom)
.PHONY: build
build:
	@readlink -e . | python3 setup.py
	@cp Aplicacion_financiera.desktop ~/.local/share/applications
	@mv Aplicacion_financiera.desktop ~/Escritorio
# @chmod +x ~/Escritorio/Aplicacion_financiera.desktop
