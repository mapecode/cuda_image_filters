DIREXE := exec/
DIRSRC := src/
CC := nvcc
RUN = python3.7

clean:
	rm -rf $(DIREXE)	


dirs:
	mkdir -p $(DIREXE)	
	cp -r src/ $(DIREXE)

format:
	autopep8 --in-place --aggressive --aggressive --recursive src/*

gaussian_kernel:
	$(RUN) $(DIREXE)src/create_kernel.py

gaussian: clean dirs gaussian_kernel
	cp $(img) $(DIREXE)	
	$(RUN) $(DIREXE)src/main.py --gaussian $(img)

grayscale: clean dirs
	cp $(img) $(DIREXE)	
	$(RUN) $(DIREXE)src/main.py --grayscale $(img)

blue: clean dirs
	cp $(img) $(DIREXE)	
	$(RUN) $(DIREXE)src/main.py --blue $(img)
