CHAR2TAPE = $(shell pwd)/../assembler/src_char2tape/char2tape
export CHAR2TAPE
SIM = $(shell pwd)/../simulator/src_c/simulator
export SIM

DIRS = $(wildcard */)
# DIRS = 10_pnl/
INPUT_103S = $(foreach dir, $(DIRS), $(dir)input.103)
INPUT_BINS = $(foreach dir, $(DIRS), $(dir)input.bin)
OUTPUT_103S = $(foreach dir, $(DIRS), $(dir)output.103)
OUTPUT_BINS = $(foreach dir, $(DIRS), $(dir)output.bin)
TASK_SEQS = $(foreach dir, $(DIRS), $(dir)task.seq)

all:
	@echo "make each|merge"

each:
	@for i  in $(DIRS); \
	do \
	make -C $$i; \
	done

merge:
	cat $(INPUT_103S) >input.103
	cat $(INPUT_BINS) >input.bin
	cat $(OUTPUT_103S) >output.103
	cat $(OUTPUT_BINS) >output.bin
	cat $(TASK_SEQS) >task.seq

