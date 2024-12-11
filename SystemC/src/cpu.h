#ifndef _CPU_H
#define _CPU_H

#include "systemc.h"

#include "pe.h"

SC_MODULE(CPU)
{   
    sc_in<bool> clk_i;

    PE pe;

    SC_HAS_PROCESS(CPU);
    
    CPU(sc_module_name nm);
    ~CPU();
    
    void mainThread();
private:

    void bus_write(int addr, int data);
    int  bus_read(int addr);

};


#endif
