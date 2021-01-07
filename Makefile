DIREXE := exec/
DIRSRC := src/
CC := nvcc
RUN = python3.7

clean:
	rm -rf $(DIREXE)	


dirs:
	mkdir -p $(DIREXE)	
	cp -r src/ $(DIREXE)
	cp -r cuda/ $(DIREXE)

format:
	autopep8 --in-place --aggressive --aggressive --recursive src/*

kernel: dirs
	$(RUN) $(DIREXE)src/create_kernel.py --gaussian

blur: dirs
	cp $(img) $(DIREXE)	
	$(RUN) $(DIREXE)src/main.py  -b $(img)
