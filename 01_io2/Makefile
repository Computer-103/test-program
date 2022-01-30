all:
	python3 helper.py >input.103
	$(CHAR2TAPE) input.103 -o input.bin
	$(SIM) -d -D input.bin
	$(CHAR2TAPE) output.103 -o output.bin
