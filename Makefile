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

blur: clean dirs
	cp $(img) $(DIREXE)	
	$(RUN) $(DIREXE)src/main.py  $(options) $(img)

sobel_sol:
	./$(DIREXE)sobel