from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from generation import generate_ai_image, generate_ai_text

import app.keyboards as kb

router = Router()

class Generate(StatesGroup):
    correct_write = State()
    generation_image = State()
    generation_text = State()
    back_state = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Generate.correct_write)
    await message.answer(f"Приветствую, здесь вы сможете сгенирировать фотографию и текст. Для большей информации, напишите команду /info") 

@router.message(Generate.correct_write, Command('info'))
async def get_info(message: Message):
    await message.answer("Снизу представлены кнопки для выбора генерации", reply_markup=kb.generation_image_text)     

@router.message(F.text == 'Сгенерировать фото')
async def user_generation_image(message: Message, state: FSMContext):
    await state.set_state(Generate.generation_image)
    await message.answer("Введите запрос для генериации вашей фотографии", reply_markup=ReplyKeyboardRemove())  

@router.message(Generate.generation_image)
async def generation(message: Message, state: FSMContext):
    prompt = message.text
    if prompt == 'Главное меню':
        await message.answer("Вы вернулись в главное меню!", reply_markup=kb.generation_image_text)
        await state.set_state(Generate.correct_write)
    else:     
        await message.reply("Идет процесс генерации фото, пожалуйста подождите!")
        image = generate_ai_image(prompt)[0]
        await message.answer_photo(photo=image,  caption='Ваше фото', reply_markup=kb.back_button)

@router.message(F.text == 'Сгенерировать текст')
async def user_generation_text(message: Message, state: FSMContext):
    await state.set_state(Generate.generation_text)
    await message.answer("Введите запрос для генерации текст", reply_markup=ReplyKeyboardRemove())

@router.message(Generate.generation_text)
async def gene(message: Message, state: FSMContext):
    prompt = message.text
    if prompt == 'Главное меню':
        await message.answer("Вы вернулись в главное меню!", reply_markup=kb.generation_image_text)
        await state.set_state(Generate.correct_write)
    else:
        await message.reply("Идет процесс обработки вашего запроса, пожалуйста подождите!")
        prompt_text = generate_ai_text(prompt)
        await message.answer(prompt_text, reply_markup=kb.back_button)

@router.message(Generate.correct_write)
async def correct(message: Message, state: FSMContext):
    await message.answer("Нажми на кнопку!")
