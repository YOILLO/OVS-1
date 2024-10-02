from torch import nn, optim
import torch
import torchgen

import model
import random
import data

import time
import operator

from data import what_figure

random.seed(0)


learn_rate = 0.0001

num_of_epoch = 1000

dataset = data.generate_dataset(3)

random.shuffle(dataset)

train_data = dataset[:int(len(dataset) * 0.80)]
test_data = dataset[int(len(dataset) * 0.80):]

train_model = model.Model1(1, [30])

loss_func = nn.CrossEntropyLoss()
optimizer = optim.Adam(train_model.parameters(), lr=learn_rate)

file = open("variant1/model1.txt", "w")

for epoch in range(num_of_epoch):
    acc = 0
    summ = 0
    num = 0
    times = 0
    for inp, outp in train_data:

        optimizer.zero_grad()

        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(torch.FloatTensor(inp_flat))
        times += time.time() - start_time

        loss = loss_func(result, torch.FloatTensor(outp))

        loss.backward()
        optimizer.step()

        acc += data.what_figure(result) == data.what_figure(outp)
        summ += loss.item()
        num += 1

    summ_test = 0
    num_test = 0
    time_test = 0
    acc_test = 0

    with torch.no_grad():
        train_model.eval()
        for inp, outp in test_data:

            optimizer.zero_grad()

            inp_flat = []

            for i in inp:
                inp_flat += i

            start_time = time.time()
            result = train_model.forward(torch.FloatTensor(inp_flat))
            time_test += time.time() - start_time
            #print(result, torch.LongTensor(outp))

            loss = loss_func(result, torch.FloatTensor(outp))

            acc_test += data.what_figure(result) == data.what_figure(outp)
            summ_test += loss.item()
            num_test += 1

    train_model.train()

    print(epoch, summ / num, times / num, acc / num, summ_test / num_test, time_test / num_test, acc_test / num)
    file.write(str(epoch))
    file.write(" ")
    file.write(str(summ / num))
    file.write(" ")
    file.write(str(times / num))
    file.write(" ")
    file.write(str(acc / num))
    file.write(" ")
    file.write(str(summ_test / num_test))
    file.write(" ")
    file.write(str(time_test / num_test))
    file.write(" ")
    file.write(str(acc_test / num_test))
    file.write("\n")

file.close()
torch.save(train_model.state_dict(), f"save1.mod")

train_model = model.Model1(2, [30, 30])

loss_func = nn.CrossEntropyLoss()
optimizer = optim.Adam(train_model.parameters(), lr=learn_rate)

file = open("variant1/model2.txt", "w")

for epoch in range(num_of_epoch):
    acc = 0
    summ = 0
    num = 0
    times = 0
    for inp, outp in train_data:

        optimizer.zero_grad()

        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(torch.FloatTensor(inp_flat))
        times += time.time() - start_time

        loss = loss_func(result, torch.FloatTensor(outp))

        loss.backward()
        optimizer.step()

        acc += data.what_figure(result) == data.what_figure(outp)
        summ += loss.item()
        num += 1

    summ_test = 0
    num_test = 0
    time_test = 0
    acc_test = 0

    with torch.no_grad():
        train_model.eval()
        for inp, outp in test_data:

            optimizer.zero_grad()

            inp_flat = []

            for i in inp:
                inp_flat += i

            start_time = time.time()
            result = train_model.forward(torch.FloatTensor(inp_flat))
            time_test += time.time() - start_time
            #print(result, torch.LongTensor(outp))

            loss = loss_func(result, torch.FloatTensor(outp))

            acc_test += data.what_figure(result) == data.what_figure(outp)
            summ_test += loss.item()
            num_test += 1

    train_model.train()

    print(epoch, summ / num, times / num, acc / num, summ_test / num_test, time_test / num_test, acc_test / num)
    file.write(str(epoch))
    file.write(" ")
    file.write(str(summ / num))
    file.write(" ")
    file.write(str(times / num))
    file.write(" ")
    file.write(str(acc / num))
    file.write(" ")
    file.write(str(summ_test / num_test))
    file.write(" ")
    file.write(str(time_test / num_test))
    file.write(" ")
    file.write(str(acc_test / num_test))
    file.write("\n")

file.close()
torch.save(train_model.state_dict(), f"save2.mod")

train_model = model.Model1(3, [30, 30, 30])

loss_func = nn.CrossEntropyLoss()
optimizer = optim.Adam(train_model.parameters(), lr=learn_rate)

file = open("variant1/model3.txt", "w")

for epoch in range(num_of_epoch):
    acc = 0
    summ = 0
    num = 0
    times = 0
    for inp, outp in train_data:

        optimizer.zero_grad()

        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(torch.FloatTensor(inp_flat))
        times += time.time() - start_time

        loss = loss_func(result, torch.FloatTensor(outp))

        loss.backward()
        optimizer.step()

        acc += data.what_figure(result) == data.what_figure(outp)
        summ += loss.item()
        num += 1

    summ_test = 0
    num_test = 0
    time_test = 0
    acc_test = 0

    with torch.no_grad():
        train_model.eval()
        for inp, outp in test_data:

            optimizer.zero_grad()

            inp_flat = []

            for i in inp:
                inp_flat += i

            start_time = time.time()
            result = train_model.forward(torch.FloatTensor(inp_flat))
            time_test += time.time() - start_time
            #print(result, torch.LongTensor(outp))

            loss = loss_func(result, torch.FloatTensor(outp))

            acc_test += data.what_figure(result) == data.what_figure(outp)
            summ_test += loss.item()
            num_test += 1

    train_model.train()

    print(epoch, summ / num, times / num, acc / num, summ_test / num_test, time_test / num_test, acc_test / num)
    file.write(str(epoch))
    file.write(" ")
    file.write(str(summ / num))
    file.write(" ")
    file.write(str(times / num))
    file.write(" ")
    file.write(str(acc / num))
    file.write(" ")
    file.write(str(summ_test / num_test))
    file.write(" ")
    file.write(str(time_test / num_test))
    file.write(" ")
    file.write(str(acc_test / num_test))
    file.write("\n")

file.close()
torch.save(train_model.state_dict(), f"save3.mod")


