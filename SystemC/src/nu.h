#ifndef _NU_H
#define _NU_H

#include "systemc.h"

SC_MODULE(NU)
{
    sc_in<bool>  clk_i;
    sc_out<int>  num;
    sc_in<int>   data;
    sc_in<int>   config;

    SC_HAS_PROCESS(NU);
    
    NU(sc_module_name nm);
    NU();
    ~NU();

private:
    int weights_mem[8];
    int value_mem[8];

    void mainThread();

    void saveToMem(int adress);
    void loadWeights(int adress);
    void pass();
    void use(int adress);
};


#endif
