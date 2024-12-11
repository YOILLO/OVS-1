#include "pe.h"

PE::PE(sc_module_name nm)
    :sc_module(nm),
    clk_i("clk_i"),
    num("num"),
    data("data"),
    config("config"),
    config_signals(NUM_OF_NU),
    data_signals(NUM_OF_NU)
{
    SC_CTHREAD(mainThread, clk_i.pos());

    for (int i = 0; i < NUM_OF_NU; i++)
    {
        nu[i].config(config_signals[i]);
        nu[i].data(data_signals[i]);
        nu[i].clk_i(clk_i);
    }
}

PE::~PE()
{ }

void PE::mainThread()
{
    resendConfig();
}

void PE::resendConfig()
{
    for (int i = 0; i < NUM_OF_NU; i++)
    {
        config_signals[i].write(config->read()[i]);
    }
}


void PE::commutation()
{
    for (int i = 0; i < NUM_OF_NU; i++)
    {
        if (commutation_config.read()[i] < NUM_OF_NU)
            data_signals[commutation_config.read()[i]].write(nu[i].num.read());
        else if (commutation_config.read()[i] == OUT_READ)
            num.write(nu[i].num.read());
        else if (commutation_config.read()[i] == IN_READ)
            data_signals[i].write(data.read());

    }
}
