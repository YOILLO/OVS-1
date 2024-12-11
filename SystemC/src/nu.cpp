#include "nu.h"

#define SAVE_TO_MEM 0
#define LOAD_WEIGHTS 1
#define PASS 2
#define USE 3

NU::NU()
    : NU("nu")
{ }

NU::NU(sc_module_name nm)
    :sc_module(nm),
    clk_i("clk_i"),
    num("num"),
    data("data"),
    config("config")
{
    SC_CTHREAD(mainThread, clk_i.pos());
}

NU::~NU()
{ }

void NU::mainThread()
{
    int config_tmp = config.read();
    if (config_tmp)
    {
        int command = (config_tmp >> 3) & 0x3;
        int adress = config_tmp & 0x7;
        switch (command)
        {
        case SAVE_TO_MEM:
            saveToMem(adress);
            break;
        case LOAD_WEIGHTS:
            loadWeights(adress);
            break;
        case PASS:
            pass();
            break;
        case USE:
            use(adress);
            break;
        default:
            SC_REPORT_ERROR("nu", "Wrong neural unit config");
            break;
        }
    }
}

void NU::saveToMem(int adress)
{ 
    num.write(value_mem[adress]);
    value_mem[adress] = data.read();
}

void NU::loadWeights(int adress)
{ weights_mem[adress] = data.read(); }

void NU::pass()
{ num.write(data.read()); }

void NU::use(int adress)
{ num.write(data.read() * weights_mem[adress]); }
