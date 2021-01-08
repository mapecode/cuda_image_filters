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

gaussian: dirs gaussian_kernel
	cp $(img) $(DIREXE)	
	$(RUN) $(DIREXE)src/main.py --gaussian $(img)
