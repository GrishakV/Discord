import discord
import math

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    await client.change_presence(status=discord.Status.online, activity=discord.Game('!!помощь/!!help developed \
    by Hustle Castle RU'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!!портал':
        await message.channel.send(f'А шо считать?')
    elif message.content.startswith('!!портал'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        if len(info) < 1 or info[0] is None:
            await message.channel.send(f'Вы не указали уровень фарма, значение по умолчанию = 80')
            lvl = 80
        else:
            lvl = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'Вы не указали необходимое количество душ, значение по умолчанию = 10000')
            total_souls = 10000
        else:
            total_souls = info[1]
        if len(info) < 3 or info[2] is None:
            souls_has = 0
        else:
            souls_has = info[2]
        if len(info) < 4 or info[3] is None:
            banner_lvl = 0
        else:
            banner_lvl = info[3]
        if len(info) < 5 or info[4] is None:
            hunters_lvl = 0
        else:
            hunters_lvl = info[4]
        if len(info) < 6 or info[5] is None:
            factor_lvl = 0
        else:
            factor_lvl = info[5]

        apples = {
            1: 8300, 2: 8500, 3: 8800, 4: 9100, 5: 9400, 6: 9700, 7: 10000, 8: 10200, 9: 10500, 10: 10800, 11: 11100,
            12: 11400, 13: 11700, 14: 11900, 15: 12200, 16: 12500, 17: 12900, 18: 13300, 19: 13700, 20: 14100,
            21: 14500, 22: 14900, 23: 15300, 24: 15700, 25: 16100, 26: 16500, 27: 16900, 28: 17300, 29: 17700,
            30: 18100, 31: 18500, 32: 18900, 33: 19400, 34: 19800, 35: 20200, 36: 20700, 37: 21100, 38: 21500,
            39: 22000, 40: 22400, 41: 22800, 42: 23300, 43: 23700, 44: 24100, 45: 24600, 46: 25000, 47: 25800,
            48: 26700, 49: 27500, 50: 28300, 51: 29200, 52: 30000, 53: 30800, 54: 31700, 55: 32500, 56: 33300,
            57: 34200, 58: 35000, 59: 35800, 60: 36700, 61: 37500, 62: 38400, 63: 39300, 64: 40300, 65: 41200,
            66: 42100, 67: 43000, 68: 43900, 69: 44900, 70: 45800, 71: 46700, 72: 47600, 73: 48600, 74: 49500,
            75: 50400, 76: 51300, 77: 52200, 78: 53200, 79: 54100, 80: 55000, 81: 56000, 82: 56900, 83: 57800,
            84: 58700, 85: 59700, 86: 60600, 87: 61500, 88: 62500, 89: 63400, 90: 64300, 91: 65300, 92: 66200,
            93: 67100, 94: 68000, 95: 69900, 96: 69900, 97: 70800, 98: 71800, 99: 72700, 100: 73600, 101: 74600,
            102: 75500, 103: 76400, 104: 77300, 105: 78300, 106: 79200, 107: 80100, 108: 81400, 109: 82000, 110: 82900,
            111: 83900, 112: 84800, 113: 85700, 114: 86600, 115: 87600, 116: 88500, 117: 89400, 118: 90400, 119: 91300,
            120: 92200, 121: 93200, 122: 94100, 123: 95000, 124: 95900, 125: 96900
        }

        souls = {
            1: 10, 2: 11, 3: 13, 4: 14, 5: 15, 6: 17, 7: 18, 8: 19, 9: 21, 10: 22, 11: 23, 12: 25, 13: 26, 14: 27,
            15: 29, 16: 30, 17: 32, 18: 34, 19: 36, 20: 38, 21: 40, 22: 42, 23: 44, 24: 46, 25: 48, 26: 50, 27: 52,
            28: 54, 29: 56, 30: 58, 31: 60, 32: 64, 33: 68, 34: 72, 35: 76, 36: 80, 37: 84, 38: 88, 39: 92, 40: 96,
            41: 100, 42: 104, 43: 108, 44: 112, 45: 116, 46: 120, 47: 128, 48: 136, 49: 144, 50: 152, 51: 160, 52: 168,
            53: 176, 54: 184, 55: 192, 56: 200, 57: 208, 58: 216, 59: 224, 60: 232, 61: 240, 62: 254, 63: 267, 64: 281,
            65: 295, 66: 308, 67: 322, 68: 336, 69: 349, 70: 363, 71: 377, 72: 391, 73: 404, 74: 418, 75: 432, 76: 445,
            77: 459, 78: 473, 79: 486, 80: 500, 81: 518, 82: 519, 83: 528, 84: 538, 85: 547, 86: 557, 87: 567, 88: 578,
            89: 586, 90: 596, 91: 605, 92: 615, 93: 625, 94: 635, 95: 645, 96: 654, 97: 664, 98: 674, 99: 684, 100: 695,
            101: 705, 102: 715, 103: 725, 104: 735, 105: 745, 106: 756, 107: 766, 108: 776, 109: 787, 110: 797,
            111: 808, 112: 818, 113: 829, 114: 840, 115: 850, 116: 861, 117: 872, 118: 882, 119: 893, 120: 904,
            121: 915, 122: 926, 123: 937, 124: 948, 125: 959
        }

        hunters = {1: 0.04, 2: 0.05, 3: 0.05, 4: 0.07, 5: 0.07, 6: 0.09}

        banner = {1: 0.05, 2: 0.07, 3: 0.09, 4: 0.11, 5: 0.13, 6: 0.15, 7: 0.20, 8: 0.25, 9: 0.30, 10: 0.37, 11: 0.44}

        factor = {0: 0, 1: 0, 2: 1, 3: 2}

        if lvl == 0:
            apples = apples[0]
            souls = souls[0]
        else:
            for i in apples:
                if i == lvl:
                    apples = apples[i]

            for j in souls:
                if j == lvl:
                    souls = souls[j]

        if banner_lvl == 0:
            banner = 0
        else:
            for b in banner:
                if b == banner_lvl:
                    banner = banner[b]

        if hunters_lvl == 0:
            hunters = 0
        else:
            for h in hunters:
                if h == hunters_lvl:
                    hunters = hunters[h]

        if factor_lvl == 0:
            factor = 0
        else:
            for f in factor:
                if f == factor_lvl:
                    factor = factor[f]

        souls = souls + souls * factor + souls * hunters + souls * banner
        tries = math.ceil((total_souls - souls_has) / souls)
        apples *= tries

        await message.channel.send(
            f"Уровень фарма: {lvl}\n"
            f"Текущее количество душ: {souls_has}\n"
            f"Желаемое количество душ: {total_souls}\n"
            f"Душ за уровень: {souls}\n"
            f"Необходимо попыток: {tries}\n"
            f"Необходимо яблок: {apples}"
        )

    if message.content == '!!добыча':
        await message.channel.send(f'А шо считать?')
    elif message.content.startswith('!!добыча'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        float_apple = info[0]
        persent_buff = info[1]

        cooking = round(((float_apple + float_apple * (persent_buff / 100)) * 24), 2)
        await message.channel.send(f"Вы добываете {cooking} яблок в сутки")

    if message.content == '!!уворот':
        await message.channel.send(f'А шо считать?')
    elif message.content.startswith('!!уворот'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        dodge = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'Вы не ввели уровни бойцов, значение по умолчанию = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_dodge = {
            1: 4036, 2: 4359, 3: 4682, 4: 5004, 5: 5327, 6: 5650, 7: 5973, 8: 6296, 9: 6619, 10: 6942, 11: 7265,
            12: 7587, 13: 7910, 14: 8233, 15: 8556, 16: 8879, 17: 9202, 18: 9525, 19: 9848, 20: 10170, 21: 10439,
            22: 10846, 23: 11139, 24: 11462, 25: 11785, 26: 12108, 27: 12430, 28: 12753, 29: 13076, 30: 13399,
            31: 13722, 32: 14045, 33: 14368, 34: 14691, 35: 15013, 36: 15336, 37: 15659, 38: 15982, 39: 16305,
            40: 16628, 41: 16951, 42: 17274, 43: 17596, 44: 17919, 45: 18242, 46: 18565, 47: 18888, 48: 19211,
            49: 19534, 50: 19857, 51: 20179, 52: 20502, 53: 20825, 54: 21148, 55: 21471, 56: 21794, 57: 22117,
            58: 22439, 59: 22762, 60: 23085, 61: 23408, 62: 23731, 63: 24054, 64: 24377, 65: 24700, 66: 25022,
            67: 25345, 68: 25668, 69: 25991, 70: 26314, 71: 26637, 72: 26960, 73: 27283, 74: 27605, 75: 27928,
            76: 28251, 77: 28574, 78: 28897, 79: 29220, 80: 29543, 81: 29865, 82: 30188, 83: 30511, 84: 30834,
            85: 31157, 86: 31480, 87: 31803, 88: 32126, 89: 32448, 90: 32771, 91: 33094, 92: 33417, 93: 33740,
            94: 34063, 95: 34386, 96: 34709, 97: 35031, 98: 35354, 99: 35677, 100: 36000
        }

        hidden_crit = {
            1: 3374, 2: 3644, 3: 3914, 4: 4184, 5: 4454, 6: 4724, 7: 4994, 8: 5264, 9: 5534, 10: 5804, 11: 6074,
            12: 6344, 13: 6614, 14: 6884, 15: 7154, 16: 7424, 17: 7694, 18: 7964, 19: 8234, 20: 8504, 21: 8774,
            22: 9043, 23: 9313, 24: 9583, 25: 9853, 26: 10123, 27: 10393, 28: 10663, 29: 10933, 30: 11203, 31: 11473,
            32: 11743, 33: 12013, 34: 12283, 35: 12553, 36: 12823, 37: 13093, 38: 13363, 39: 13633, 40: 13903,
            41: 14173, 42: 14443, 43: 14713, 44: 14983, 45: 15252, 46: 15522, 47: 15792, 48: 16062, 49: 16332,
            50: 16602, 51: 16872, 52: 17142, 53: 17412, 54: 17682, 55: 17952, 56: 18222, 57: 18492, 58: 18762,
            59: 19032, 60: 19302, 61: 19572, 62: 19842, 63: 20112, 64: 20382, 65: 20652, 66: 20922, 67: 21191,
            68: 21461, 69: 21731, 70: 22001, 71: 22271, 72: 22541, 73: 22811, 74: 23081, 75: 23351, 76: 23621,
            77: 23891, 78: 24161, 79: 24431, 80: 24701, 81: 24971, 82: 25241, 83: 25511, 84: 25781, 85: 26051,
            86: 26321, 87: 26591, 88: 26861, 89: 27130, 90: 27400, 91: 27670, 92: 27940, 93: 28210, 94: 28480,
            95: 28750, 96: 29020, 97: 29290, 98: 29560, 99: 29830, 100: 30100
        }

        for d in hidden_dodge:
            if d == fighter_lvl:
                fighter_dodge = hidden_dodge[d]
            if d == enemy_lvl:
                enemy_dodge = hidden_dodge[d]

        for c in hidden_crit:
            if c == fighter_lvl:
                fighter_crit = hidden_crit[c]
            if c == enemy_lvl:
                enemy_crit = hidden_crit[c]

        dodge_res = 1 - fighter_dodge / (enemy_dodge + enemy_dodge * (1 - enemy_crit / (enemy_crit + dodge)))
        dodge_result = round(dodge_res * 100, 2)

        await message.channel.send(f"Шанс увернуться от атаки = {dodge_result}%")

    if message.content == '!!крит':
        await message.channel.send(f'А шо считать?')
    elif message.content.startswith('!!крит'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        crit = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'Вы не ввели уровни бойцов, значение по умолчанию = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_crit = {
            1: 3374, 2: 3644, 3: 3914, 4: 4184, 5: 4454, 6: 4724, 7: 4994, 8: 5264, 9: 5534, 10: 5804, 11: 6074,
            12: 6344, 13: 6614, 14: 6884, 15: 7154, 16: 7424, 17: 7694, 18: 7964, 19: 8234, 20: 8504, 21: 8774,
            22: 9043, 23: 9313, 24: 9583, 25: 9853, 26: 10123, 27: 10393, 28: 10663, 29: 10933, 30: 11203, 31: 11473,
            32: 11743, 33: 12013, 34: 12283, 35: 12553, 36: 12823, 37: 13093, 38: 13363, 39: 13633, 40: 13903,
            41: 14173, 42: 14443, 43: 14713, 44: 14983, 45: 15252, 46: 15522, 47: 15792, 48: 16062, 49: 16332,
            50: 16602, 51: 16872, 52: 17142, 53: 17412, 54: 17682, 55: 17952, 56: 18222, 57: 18492, 58: 18762,
            59: 19032, 60: 19302, 61: 19572, 62: 19842, 63: 20112, 64: 20382, 65: 20652, 66: 20922, 67: 21191,
            68: 21461, 69: 21731, 70: 22001, 71: 22271, 72: 22541, 73: 22811, 74: 23081, 75: 23351, 76: 23621,
            77: 23891, 78: 24161, 79: 24431, 80: 24701, 81: 24971, 82: 25241, 83: 25511, 84: 25781, 85: 26051,
            86: 26321, 87: 26591, 88: 26861, 89: 27130, 90: 27400, 91: 27670, 92: 27940, 93: 28210, 94: 28480,
            95: 28750, 96: 29020, 97: 29290, 98: 29560, 99: 29830, 100: 30100
        }

        for c in hidden_crit:
            if c == fighter_lvl:
                fighter_crit = hidden_crit[c]
            if c == enemy_lvl:
                enemy_crit = hidden_crit[c]

        crit_res = 1 - enemy_crit / (fighter_crit + crit)
        crit_result = round(crit_res * 100, 2)

        await message.channel.send(f"Шанс нанести критический урон = {crit_result}%")

    if message.content == '!!магброня':
        await message.channel.send(f'А шо считать?')
    elif message.content.startswith('!!магброня'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        mage_armor = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'Вы не ввели уровни бойцов, значение по умолчанию = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_mage_armor = {
            1: 3364, 2: 3632, 3: 3901, 4: 4170, 5: 4440, 6: 4709, 7: 4978, 8: 5246, 9: 5515, 10: 5785, 11: 6054,
            12: 6323, 13: 6592, 14: 6860, 15: 7130, 16: 7399, 17: 7668, 18: 7937, 19: 8207, 20: 8476, 21: 8744,
            22: 9013, 23: 9282, 24: 9552, 25: 9821, 26: 10090, 27: 10358, 28: 10628, 29: 10897, 30: 11166, 31: 11435,
            32: 11704, 33: 11974, 34: 12242, 35: 12511, 36: 12780, 37: 13049, 38: 13319, 39: 13588, 40: 13856,
            41: 14125, 42: 14395, 43: 14664, 44: 14933, 45: 15202, 46: 15470, 47: 15740, 48: 16009, 49: 16278,
            50: 16547, 51: 16816, 52: 17086, 53: 17354, 54: 17623, 55: 17892, 56: 18162, 57: 18431, 58: 18700,
            59: 18968, 60: 19237, 61: 19507, 62: 19776, 63: 20045, 64: 20314, 65: 20582, 66: 20852, 67: 21121,
            68: 21390, 69: 21659, 70: 21929, 71: 22198, 72: 22466, 73: 22735, 74: 23004, 75: 23274, 76: 23543,
            77: 23812, 78: 24080, 79: 24349, 80: 24619, 81: 24888, 82: 25157, 83: 25426, 84: 25696, 85: 25964,
            86: 26233, 87: 26502, 88: 26771, 89: 27041, 90: 27310, 91: 27578, 92: 27847, 93: 28116, 94: 28386,
            95: 28655, 96: 28924, 97: 29192, 98: 29462, 99: 29731, 100: 30000
        }

        for a in hidden_mage_armor:
            if a == fighter_lvl:
                fighter_mage_armor = hidden_mage_armor[a]
            if a == enemy_lvl:
                enemy_mage_armor = hidden_mage_armor[a]

        mage_armor_res = 1 - fighter_mage_armor / (enemy_mage_armor + mage_armor)
        mage_armor_result = round(mage_armor_res * 100, 2)

        await message.channel.send(f"Поглощение магического урона = {mage_armor_result}%")

    if message.content == '!!броня':
        await message.channel.send(f'А шо считать?')
    elif message.content.startswith('!!броня'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        armor = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'Вы не ввели уровни бойцов, значение по умолчанию = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_armor = {
            1: 3442, 2: 3717, 3: 3992, 4: 4268, 5: 4543, 6: 4818, 7: 5094, 8: 5369, 9: 5644, 10: 5920, 11: 6195,
            12: 6470, 13: 6746, 14: 7021, 15: 7296, 16: 7572, 17: 7847, 18: 8122, 19: 8398, 20: 8673, 21: 8948,
            22: 9224, 23: 9499, 24: 9774, 25: 10050, 26: 10325, 27: 10600, 28: 10876, 29: 11151, 30: 11426, 31: 11702,
            32: 11977, 33: 12252, 34: 12528, 35: 12803, 36: 13078, 37: 13354, 38: 13629, 39: 13904, 40: 14180,
            41: 14455, 42: 14730, 43: 15006, 44: 15281, 45: 15557, 46: 15832, 47: 16107, 48: 16383, 49: 16658,
            50: 16933, 51: 17209, 52: 17484, 53: 17759, 54: 18035, 55: 18310, 56: 18585, 57: 18861, 58: 19136,
            59: 19411, 60: 19687, 61: 19962, 62: 20237, 63: 20513, 64: 20788, 65: 21063, 66: 21339, 67: 21614,
            68: 21889, 69: 22165, 70: 22440, 71: 22715, 72: 22991, 73: 23266, 74: 23541, 75: 23817, 76: 24092,
            77: 24367, 78: 24643, 79: 24918, 80: 25193, 81: 25469, 82: 25744, 83: 26019, 84: 26295, 85: 26570,
            86: 26845, 87: 27121, 88: 27396, 89: 27671, 90: 27947, 91: 28222, 92: 28497, 93: 28773, 94: 29048,
            95: 29323, 96: 29599, 97: 29874, 98: 30149, 99: 30425, 100: 30700
        }

        for a in hidden_armor:
            if a == fighter_lvl:
                fighter_armor = hidden_armor[a]
            if a == enemy_lvl:
                enemy_armor = hidden_armor[a]

        armor_res = 1 - fighter_armor / (enemy_armor + armor)
        armor_result = round(armor_res * 100, 2)

        await message.channel.send(f"Поглощение физического урона = {armor_result}%")

    if message.content == '!!бот':
        await message.channel.send(f"Доступные команды:\n"
                                   f"1. !!портал\n"
                                   f"2. !!добыча\n"
                                   f"3. !!броня\n"
                                   f"4. !!магброня\n"
                                   f"5. !!уворот\n"
                                   f"6. !!крит\n"
                                   f"7. !!помощь"
                                   )

    if message.content == '!!помощь':
        await message.author.send(f'''
        Для использования бота нужно написать в чат:

1. Для того, чтобы узнать свою добычу в сутки(из любой комнаты) ввести:
**!!добыча** добыча в час,%бонус добычи
(например: !!добыча 84496,24)
2. Для того, чтобы использовать калькулятор портала ввести:
**!!портал** уровень фарма,необходимое количество душ,сколько душ у вас уже есть,уровень
знамени душ, уровень квартала охотников,множитель(0-без множителя, 1-х2, 2-х3
(например: !!портал 125,1000000,100000,11,6,2)
3. Для того, чтобы узнать % поглощения брони, маг брони,шанса уворота,шанса крита,
необходимо ввести соответственно команду **!!броня !!магброня !!крит !!уворот** значение
соответствующего стата,уровень вашего бойца, уровень вражеского бойца
(например: !!броня 10000,100,100 !!магброня 15000,100,100 и т.д)
Если вы хотите оставить поле пустым(например, идёте в портал без знамени душ), то
просто в этом месте введите **0**.Необходимо правильно вводить команду, после неё
пробел, затем перечислить данные через запятую,
в указанной последовательности.
        ''')

    if message.content == '!!portal':
        await message.channel.send(f'Please, enter values')
    elif message.content.startswith('!!portal'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        if len(info) < 1 or info[0] is None:
            await message.channel.send(f'You did not specify the level of farming, default value = 80')
            lvl = 80
        else:
            lvl = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'You did not specify the required number of souls, default value = 10000')
            total_souls = 10000
        else:
            total_souls = info[1]
        if len(info) < 3 or info[2] is None:
            souls_has = 0
        else:
            souls_has = info[2]
        if len(info) < 4 or info[3] is None:
            banner_lvl = 0
        else:
            banner_lvl = info[3]
        if len(info) < 5 or info[4] is None:
            hunters_lvl = 0
        else:
            hunters_lvl = info[4]
        if len(info) < 6 or info[5] is None:
            factor_lvl = 0
        else:
            factor_lvl = info[5]

        apples = {
            1: 8300, 2: 8500, 3: 8800, 4: 9100, 5: 9400, 6: 9700, 7: 10000, 8: 10200, 9: 10500, 10: 10800,
            11: 11100,
            12: 11400, 13: 11700, 14: 11900, 15: 12200, 16: 12500, 17: 12900, 18: 13300, 19: 13700, 20: 14100,
            21: 14500, 22: 14900, 23: 15300, 24: 15700, 25: 16100, 26: 16500, 27: 16900, 28: 17300, 29: 17700,
            30: 18100, 31: 18500, 32: 18900, 33: 19400, 34: 19800, 35: 20200, 36: 20700, 37: 21100, 38: 21500,
            39: 22000, 40: 22400, 41: 22800, 42: 23300, 43: 23700, 44: 24100, 45: 24600, 46: 25000, 47: 25800,
            48: 26700, 49: 27500, 50: 28300, 51: 29200, 52: 30000, 53: 30800, 54: 31700, 55: 32500, 56: 33300,
            57: 34200, 58: 35000, 59: 35800, 60: 36700, 61: 37500, 62: 38400, 63: 39300, 64: 40300, 65: 41200,
            66: 42100, 67: 43000, 68: 43900, 69: 44900, 70: 45800, 71: 46700, 72: 47600, 73: 48600, 74: 49500,
            75: 50400, 76: 51300, 77: 52200, 78: 53200, 79: 54100, 80: 55000, 81: 56000, 82: 56900, 83: 57800,
            84: 58700, 85: 59700, 86: 60600, 87: 61500, 88: 62500, 89: 63400, 90: 64300, 91: 65300, 92: 66200,
            93: 67100, 94: 68000, 95: 69900, 96: 69900, 97: 70800, 98: 71800, 99: 72700, 100: 73600, 101: 74600,
            102: 75500, 103: 76400, 104: 77300, 105: 78300, 106: 79200, 107: 80100, 108: 81400, 109: 82000,
            110: 82900,
            111: 83900, 112: 84800, 113: 85700, 114: 86600, 115: 87600, 116: 88500, 117: 89400, 118: 90400,
            119: 91300,
            120: 92200, 121: 93200, 122: 94100, 123: 95000, 124: 95900, 125: 96900
        }

        souls = {
            1: 10, 2: 11, 3: 13, 4: 14, 5: 15, 6: 17, 7: 18, 8: 19, 9: 21, 10: 22, 11: 23, 12: 25, 13: 26, 14: 27,
            15: 29, 16: 30, 17: 32, 18: 34, 19: 36, 20: 38, 21: 40, 22: 42, 23: 44, 24: 46, 25: 48, 26: 50, 27: 52,
            28: 54, 29: 56, 30: 58, 31: 60, 32: 64, 33: 68, 34: 72, 35: 76, 36: 80, 37: 84, 38: 88, 39: 92, 40: 96,
            41: 100, 42: 104, 43: 108, 44: 112, 45: 116, 46: 120, 47: 128, 48: 136, 49: 144, 50: 152, 51: 160,
            52: 168,
            53: 176, 54: 184, 55: 192, 56: 200, 57: 208, 58: 216, 59: 224, 60: 232, 61: 240, 62: 254, 63: 267,
            64: 281,
            65: 295, 66: 308, 67: 322, 68: 336, 69: 349, 70: 363, 71: 377, 72: 391, 73: 404, 74: 418, 75: 432,
            76: 445,
            77: 459, 78: 473, 79: 486, 80: 500, 81: 518, 82: 519, 83: 528, 84: 538, 85: 547, 86: 557, 87: 567,
            88: 578,
            89: 586, 90: 596, 91: 605, 92: 615, 93: 625, 94: 635, 95: 645, 96: 654, 97: 664, 98: 674, 99: 684,
            100: 695,
            101: 705, 102: 715, 103: 725, 104: 735, 105: 745, 106: 756, 107: 766, 108: 776, 109: 787, 110: 797,
            111: 808, 112: 818, 113: 829, 114: 840, 115: 850, 116: 861, 117: 872, 118: 882, 119: 893, 120: 904,
            121: 915, 122: 926, 123: 937, 124: 948, 125: 959
        }

        hunters = {1: 0.04, 2: 0.05, 3: 0.05, 4: 0.07, 5: 0.07, 6: 0.09}

        banner = {1: 0.05, 2: 0.07, 3: 0.09, 4: 0.11, 5: 0.13, 6: 0.15, 7: 0.20, 8: 0.25, 9: 0.30, 10: 0.37,
                  11: 0.44}

        factor = {0: 0, 1: 0, 2: 1, 3: 2}

        if lvl == 0:
            apples = apples[0]
            souls = souls[0]
        else:
            for i in apples:
                if i == lvl:
                    apples = apples[i]

            for j in souls:
                if j == lvl:
                    souls = souls[j]

        if banner_lvl == 0:
            banner = 0
        else:
            for b in banner:
                if b == banner_lvl:
                    banner = banner[b]

        if hunters_lvl == 0:
            hunters = 0
        else:
            for h in hunters:
                if h == hunters_lvl:
                    hunters = hunters[h]

        if factor_lvl == 0:
            factor = 0
        else:
            for f in factor:
                if f == factor_lvl:
                    factor = factor[f]

        souls = souls + souls * factor + souls * hunters + souls * banner
        tries = math.ceil((total_souls - souls_has) / souls)
        apples *= tries

        await message.channel.send(
            f"Farm level: {lvl}\n"
            f"Current number of souls: {souls_has}\n"
            f"Required number of souls: {total_souls}\n"
            f"Souls per level: {souls}\n"
            f"Attempts need: {tries}\n"
            f"Apples need: {apples}"
        )

    if message.content == '!!production':
        await message.channel.send(f'Please, enter values')
    elif message.content.startswith('!!production'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        float_apple = info[0]
        persent_buff = info[1]

        cooking = round(((float_apple + float_apple * (persent_buff / 100)) * 24), 2)
        await message.channel.send(f"You product {cooking} apples per day")

    if message.content == '!!dodge':
        await message.channel.send(f'Please, enter values')
    elif message.content.startswith('!!dodge'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        dodge = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'You have not entered the levels of fighters, default value = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_dodge = {
            1: 4036, 2: 4359, 3: 4682, 4: 5004, 5: 5327, 6: 5650, 7: 5973, 8: 6296, 9: 6619, 10: 6942, 11: 7265,
            12: 7587, 13: 7910, 14: 8233, 15: 8556, 16: 8879, 17: 9202, 18: 9525, 19: 9848, 20: 10170, 21: 10439,
            22: 10846, 23: 11139, 24: 11462, 25: 11785, 26: 12108, 27: 12430, 28: 12753, 29: 13076, 30: 13399,
            31: 13722, 32: 14045, 33: 14368, 34: 14691, 35: 15013, 36: 15336, 37: 15659, 38: 15982, 39: 16305,
            40: 16628, 41: 16951, 42: 17274, 43: 17596, 44: 17919, 45: 18242, 46: 18565, 47: 18888, 48: 19211,
            49: 19534, 50: 19857, 51: 20179, 52: 20502, 53: 20825, 54: 21148, 55: 21471, 56: 21794, 57: 22117,
            58: 22439, 59: 22762, 60: 23085, 61: 23408, 62: 23731, 63: 24054, 64: 24377, 65: 24700, 66: 25022,
            67: 25345, 68: 25668, 69: 25991, 70: 26314, 71: 26637, 72: 26960, 73: 27283, 74: 27605, 75: 27928,
            76: 28251, 77: 28574, 78: 28897, 79: 29220, 80: 29543, 81: 29865, 82: 30188, 83: 30511, 84: 30834,
            85: 31157, 86: 31480, 87: 31803, 88: 32126, 89: 32448, 90: 32771, 91: 33094, 92: 33417, 93: 33740,
            94: 34063, 95: 34386, 96: 34709, 97: 35031, 98: 35354, 99: 35677, 100: 36000
        }

        hidden_crit = {
            1: 3374, 2: 3644, 3: 3914, 4: 4184, 5: 4454, 6: 4724, 7: 4994, 8: 5264, 9: 5534, 10: 5804, 11: 6074,
            12: 6344, 13: 6614, 14: 6884, 15: 7154, 16: 7424, 17: 7694, 18: 7964, 19: 8234, 20: 8504, 21: 8774,
            22: 9043, 23: 9313, 24: 9583, 25: 9853, 26: 10123, 27: 10393, 28: 10663, 29: 10933, 30: 11203,
            31: 11473,
            32: 11743, 33: 12013, 34: 12283, 35: 12553, 36: 12823, 37: 13093, 38: 13363, 39: 13633, 40: 13903,
            41: 14173, 42: 14443, 43: 14713, 44: 14983, 45: 15252, 46: 15522, 47: 15792, 48: 16062, 49: 16332,
            50: 16602, 51: 16872, 52: 17142, 53: 17412, 54: 17682, 55: 17952, 56: 18222, 57: 18492, 58: 18762,
            59: 19032, 60: 19302, 61: 19572, 62: 19842, 63: 20112, 64: 20382, 65: 20652, 66: 20922, 67: 21191,
            68: 21461, 69: 21731, 70: 22001, 71: 22271, 72: 22541, 73: 22811, 74: 23081, 75: 23351, 76: 23621,
            77: 23891, 78: 24161, 79: 24431, 80: 24701, 81: 24971, 82: 25241, 83: 25511, 84: 25781, 85: 26051,
            86: 26321, 87: 26591, 88: 26861, 89: 27130, 90: 27400, 91: 27670, 92: 27940, 93: 28210, 94: 28480,
            95: 28750, 96: 29020, 97: 29290, 98: 29560, 99: 29830, 100: 30100
        }

        for d in hidden_dodge:
            if d == fighter_lvl:
                fighter_dodge = hidden_dodge[d]
            if d == enemy_lvl:
                enemy_dodge = hidden_dodge[d]

        for c in hidden_crit:
            if c == fighter_lvl:
                fighter_crit = hidden_crit[c]
            if c == enemy_lvl:
                enemy_crit = hidden_crit[c]

        dodge_res = 1 - fighter_dodge / (enemy_dodge + enemy_dodge * (1 - enemy_crit / (enemy_crit + dodge)))
        dodge_result = round(dodge_res * 100, 2)

        await message.channel.send(f"Chance to dodge an attack = {dodge_result}%")

    if message.content == '!!crit':
        await message.channel.send(f'Please, enter values')
    elif message.content.startswith('!!crit'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        crit = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'You have not entered the levels of fighters, default value = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_crit = {
            1: 3374, 2: 3644, 3: 3914, 4: 4184, 5: 4454, 6: 4724, 7: 4994, 8: 5264, 9: 5534, 10: 5804, 11: 6074,
            12: 6344, 13: 6614, 14: 6884, 15: 7154, 16: 7424, 17: 7694, 18: 7964, 19: 8234, 20: 8504, 21: 8774,
            22: 9043, 23: 9313, 24: 9583, 25: 9853, 26: 10123, 27: 10393, 28: 10663, 29: 10933, 30: 11203,
            31: 11473,
            32: 11743, 33: 12013, 34: 12283, 35: 12553, 36: 12823, 37: 13093, 38: 13363, 39: 13633, 40: 13903,
            41: 14173, 42: 14443, 43: 14713, 44: 14983, 45: 15252, 46: 15522, 47: 15792, 48: 16062, 49: 16332,
            50: 16602, 51: 16872, 52: 17142, 53: 17412, 54: 17682, 55: 17952, 56: 18222, 57: 18492, 58: 18762,
            59: 19032, 60: 19302, 61: 19572, 62: 19842, 63: 20112, 64: 20382, 65: 20652, 66: 20922, 67: 21191,
            68: 21461, 69: 21731, 70: 22001, 71: 22271, 72: 22541, 73: 22811, 74: 23081, 75: 23351, 76: 23621,
            77: 23891, 78: 24161, 79: 24431, 80: 24701, 81: 24971, 82: 25241, 83: 25511, 84: 25781, 85: 26051,
            86: 26321, 87: 26591, 88: 26861, 89: 27130, 90: 27400, 91: 27670, 92: 27940, 93: 28210, 94: 28480,
            95: 28750, 96: 29020, 97: 29290, 98: 29560, 99: 29830, 100: 30100
        }

        for c in hidden_crit:
            if c == fighter_lvl:
                fighter_crit = hidden_crit[c]
            if c == enemy_lvl:
                enemy_crit = hidden_crit[c]

        crit_res = 1 - enemy_crit / (fighter_crit + crit)
        crit_result = round(crit_res * 100, 2)

        await message.channel.send(f"Chance of dealing crit damage = {crit_result}%")

    if message.content == '!!magicarmor':
        await message.channel.send(f'Please, enter values')
    elif message.content.startswith('!!magicarmor'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        mage_armor = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'You have not entered the levels of fighters, default value = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_mage_armor = {
            1: 3364, 2: 3632, 3: 3901, 4: 4170, 5: 4440, 6: 4709, 7: 4978, 8: 5246, 9: 5515, 10: 5785, 11: 6054,
            12: 6323, 13: 6592, 14: 6860, 15: 7130, 16: 7399, 17: 7668, 18: 7937, 19: 8207, 20: 8476, 21: 8744,
            22: 9013, 23: 9282, 24: 9552, 25: 9821, 26: 10090, 27: 10358, 28: 10628, 29: 10897, 30: 11166,
            31: 11435,
            32: 11704, 33: 11974, 34: 12242, 35: 12511, 36: 12780, 37: 13049, 38: 13319, 39: 13588, 40: 13856,
            41: 14125, 42: 14395, 43: 14664, 44: 14933, 45: 15202, 46: 15470, 47: 15740, 48: 16009, 49: 16278,
            50: 16547, 51: 16816, 52: 17086, 53: 17354, 54: 17623, 55: 17892, 56: 18162, 57: 18431, 58: 18700,
            59: 18968, 60: 19237, 61: 19507, 62: 19776, 63: 20045, 64: 20314, 65: 20582, 66: 20852, 67: 21121,
            68: 21390, 69: 21659, 70: 21929, 71: 22198, 72: 22466, 73: 22735, 74: 23004, 75: 23274, 76: 23543,
            77: 23812, 78: 24080, 79: 24349, 80: 24619, 81: 24888, 82: 25157, 83: 25426, 84: 25696, 85: 25964,
            86: 26233, 87: 26502, 88: 26771, 89: 27041, 90: 27310, 91: 27578, 92: 27847, 93: 28116, 94: 28386,
            95: 28655, 96: 28924, 97: 29192, 98: 29462, 99: 29731, 100: 30000
        }

        for a in hidden_mage_armor:
            if a == fighter_lvl:
                fighter_mage_armor = hidden_mage_armor[a]
            if a == enemy_lvl:
                enemy_mage_armor = hidden_mage_armor[a]

        mage_armor_res = 1 - fighter_mage_armor / (enemy_mage_armor + mage_armor)
        mage_armor_result = round(mage_armor_res * 100, 2)

        await message.channel.send(f"Magical damage absorption = {mage_armor_result}%")

    if message.content == '!!armor':
        await message.channel.send(f'Please, enter values')
    elif message.content.startswith('!!armor'):
        msg_list = message.content.split(' ', maxsplit=1)
        msg_list[1] = msg_list[1].replace(' ', '')
        info = list(map(int, msg_list[1].split(',')))
        armor = info[0]
        if len(info) < 2 or info[1] is None:
            await message.channel.send(f'You have not entered the levels of fighters, default value = 100')
            fighter_lvl = 100
            enemy_lvl = 100
        else:
            fighter_lvl = info[2]
            enemy_lvl = info[1]

        hidden_armor = {
            1: 3442, 2: 3717, 3: 3992, 4: 4268, 5: 4543, 6: 4818, 7: 5094, 8: 5369, 9: 5644, 10: 5920, 11: 6195,
            12: 6470, 13: 6746, 14: 7021, 15: 7296, 16: 7572, 17: 7847, 18: 8122, 19: 8398, 20: 8673, 21: 8948,
            22: 9224, 23: 9499, 24: 9774, 25: 10050, 26: 10325, 27: 10600, 28: 10876, 29: 11151, 30: 11426,
            31: 11702,
            32: 11977, 33: 12252, 34: 12528, 35: 12803, 36: 13078, 37: 13354, 38: 13629, 39: 13904, 40: 14180,
            41: 14455, 42: 14730, 43: 15006, 44: 15281, 45: 15557, 46: 15832, 47: 16107, 48: 16383, 49: 16658,
            50: 16933, 51: 17209, 52: 17484, 53: 17759, 54: 18035, 55: 18310, 56: 18585, 57: 18861, 58: 19136,
            59: 19411, 60: 19687, 61: 19962, 62: 20237, 63: 20513, 64: 20788, 65: 21063, 66: 21339, 67: 21614,
            68: 21889, 69: 22165, 70: 22440, 71: 22715, 72: 22991, 73: 23266, 74: 23541, 75: 23817, 76: 24092,
            77: 24367, 78: 24643, 79: 24918, 80: 25193, 81: 25469, 82: 25744, 83: 26019, 84: 26295, 85: 26570,
            86: 26845, 87: 27121, 88: 27396, 89: 27671, 90: 27947, 91: 28222, 92: 28497, 93: 28773, 94: 29048,
            95: 29323, 96: 29599, 97: 29874, 98: 30149, 99: 30425, 100: 30700
        }

        for a in hidden_armor:
            if a == fighter_lvl:
                fighter_armor = hidden_armor[a]
            if a == enemy_lvl:
                enemy_armor = hidden_armor[a]

        armor_res = 1 - fighter_armor / (enemy_armor + armor)
        armor_result = round(armor_res * 100, 2)

        await message.channel.send(f"Physical damage absorption = {armor_result}%")

    if message.content == '!!bot':
        await message.channel.send(f"command list:\n"
                                   f"1. !!portal\n"
                                   f"2. !!production\n"
                                   f"3. !!armor\n"
                                   f"4. !!magicarmor\n"
                                   f"5. !!dodge\n"
                                   f"6. !!crit\n"
                                   f"7. !!help"
                                   )

    if message.content == '!!help':
        await message.author.send(f'''
1. Calculating production of food per day [can work with all resources] :
- the prefix is **!!production** with additional information listed in the following order
- production per hour,%production bonus [happiness]
- **e.g**: !!production 60000,20
2. To use the Portal Calculator :
- The prefix is **!!portal** All additional information is added in the following order 
- desired farming level,souls required for goal,souls currently obtained,level of soul banner,
level of hunter neighbourhood,soul multiplier [0 or 1=no multiplier, 2=x2, 3=x3]
- **e.g.**: !!portal 80,150000,10000,11,6,3
3. Determining percentages of stats :
- The following prefixes all follow the same pattern ;
**!!armor , !!magicarmor , !!crit , !!dodge**
- additional information required is added in this order .. 
stat value [found in the list to the left of an equipped item], your fighter level, opponent fighter level
- **e.g.** !!dodge: 10000,100,100
- When entering the numbers in the command, you can substitute the value as 0 
[for example you do not have banner of souls equipped]
- The bot requires all fields to be entered correctly in order to work properly.
Leave a space after the prefix, and the data separated by commas [with no spaces in between] and in the correct sequence
            ''')

# Здесь должен быть токен
client.run('token')
