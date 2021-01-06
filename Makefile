DIREXE := exec/
DIRSRC := src/
CC := nvcc

clean : 
	rm -rf *~ core $(DIREXE) $(DIRSRC)*~ 

dirs:
	mkdir -p $(DIREXE)

sobel:	
	$(CC) $(DIRSRC)sobel.cu -o $(DIREXE)sobel

sobel_sol:
	./$(DIREXE)sobel