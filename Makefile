install:
	cp startup.py ~
	sed -i '4 i python3 startup.py' ~/.bashrc
	cp starship.toml ~/.config
