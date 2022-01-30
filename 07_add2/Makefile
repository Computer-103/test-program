all:
	python3 helper.py >input.103
	$(CHAR2TAPE) input.103 -o input.bin
	-$(SIM) input.bin >/dev/null
	$(CHAR2TAPE) output.103 -o output.bin
