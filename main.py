import model
import random
import data

import time

random.seed(0)


learn_rate = 0.0001

num_of_epoch = 100

dataset = data.generate_dataset(3)

random.shuffle(dataset)

train_data = dataset[:int(len(dataset) * 0.80)]
test_data = dataset[int(len(dataset) * 0.80):]

train_model = model.Model(1, [30], learn_rate)

file = open("variant1/model1.txt", "w")

for epoch in range(num_of_epoch):
    acc = 0
    summ = 0
    num = 0
    times = 0
    for inp, outp in train_data:

        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(inp_flat)
        times += time.time() - start_time

        loss = model.find_loss(result, outp)

        train_model.backward(outp, loss)

        acc += data.what_figure(result) == data.what_figure(outp)
        summ += loss
        num += 1

    summ_test = 0
    num_test = 0
    time_test = 0
    acc_test = 0

    for inp, outp in test_data:
        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(inp_flat)
        time_test += time.time() - start_time

        loss = model.find_loss(result, outp)

        acc_test += data.what_figure(result) == data.what_figure(outp)
        summ_test += loss
        num_test += 1

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
#torch.save(train_model.state_dict(), f"save1.mod")

train_model = model.Model(2, [30, 30], learn_rate)

file = open("variant1/model2.txt", "w")

for epoch in range(num_of_epoch):
    acc = 0
    summ = 0
    num = 0
    times = 0
    for inp, outp in train_data:

        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(inp_flat)
        times += time.time() - start_time

        loss = model.find_loss(result, outp)

        train_model.backward(outp, loss)

        acc += data.what_figure(result) == data.what_figure(outp)
        summ += loss
        num += 1

    summ_test = 0
    num_test = 0
    time_test = 0
    acc_test = 0

    for inp, outp in test_data:
        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(inp_flat)
        time_test += time.time() - start_time

        loss = model.find_loss(result, outp)

        acc_test += data.what_figure(result) == data.what_figure(outp)
        summ_test += loss
        num_test += 1

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
#torch.save(train_model.state_dict(), f"save2.mod")

train_model = model.Model(3, [30, 30, 30], learn_rate)

file = open("variant1/model3.txt", "w")

for epoch in range(num_of_epoch):
    acc = 0
    summ = 0
    num = 0
    times = 0
    for inp, outp in train_data:

        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(inp_flat)
        times += time.time() - start_time

        loss = model.find_loss(result, outp)

        train_model.backward(outp, loss)

        acc += data.what_figure(result) == data.what_figure(outp)
        summ += loss
        num += 1

    summ_test = 0
    num_test = 0
    time_test = 0
    acc_test = 0

    for inp, outp in test_data:
        inp_flat = []

        for i in inp:
            inp_flat += i

        start_time = time.time()
        result = train_model.forward(inp_flat)
        time_test += time.time() - start_time

        loss = model.find_loss(result, outp)

        acc_test += data.what_figure(result) == data.what_figure(outp)
        summ_test += loss
        num_test += 1

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
#torch.save(train_model.state_dict(), f"save3.mod")


