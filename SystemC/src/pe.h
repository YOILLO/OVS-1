#ifndef _PE_H
#define _PE_H

#include "systemc.h"
#include "nu.h"

#define NUM_OF_NU 10
#define OUT_READ NUM_OF_NU
#define IN_READ NUM_OF_NU + 1

SC_MODULE(PE)
{
    sc_in<bool>  clk_i;
    sc_out<int>  num;
    sc_in<int>   data;
    sc_in<int[NUM_OF_NU]>   commutation_config;
    sc_in<int[NUM_OF_NU]>   config;

    NU nu[NUM_OF_NU];
    sc_signal<size_t> v_start_addr[NUM_OF_NU];

    std::vector<sc_signal<int>> config_signals;
    std::vector<sc_signal<int>> data_signals;

    SC_HAS_PROCESS(PE);

    PE(sc_module_name nm);
    ~PE();

private:
    void mainThread();

    void resendConfig();
    void commutation();
};


#endif
