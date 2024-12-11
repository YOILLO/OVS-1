SYSTEMC_HOME    = /home/ya/lib/systemc-2.3.3
TARGET_ARCH     = linux64

SYSTEMC_INC_DIR = $(SYSTEMC_HOME)/include
SYSTEMC_LIB_DIR = $(SYSTEMC_HOME)/lib-$(TARGET_ARCH)

FLAGS           = -g -Wall -pedantic -std=c++11 -Wno-long-long \
                 -DSC_INCLUDE_DYNAMIC_PROCESSES -fpermissive \
                 -I$(SYSTEMC_INC_DIR)
LDFLAGS         = -L$(SYSTEMC_LIB_DIR) -lsystemc -lm

SRCS = src/cpu.cpp src/mem.cpp src/main.cpp src/nu.cpp src/pe.cpp
OBJS = $(SRCS:.cpp=.o)
	
main:
	g++ -o model $(LDFLAGS) $(FLAGS) $(SRCS)

