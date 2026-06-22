import os
from dotenv import load_dotenv

load_dotenv()


class Config:


    API_TYPE = os.getenv(
        'API_TYPE',
        'mymemory'
    )


    GOOGLE_API_KEY = os.getenv(
        'GOOGLE_API_KEY',
        ''
    )


    DEBUG = os.getenv(
        'DEBUG',
        'True'
    ).lower() == 'true'


    PORT = int(
        os.getenv(
            'PORT',
            5000
        )
    )


    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'dev-secret-key'
    )



    SUPPORTED_LANGUAGES = [


        {
            'code':'en',
            'name':'English',
            'flag':'🇬🇧'
        },


        {
            'code':'te',
            'name':'Telugu',
            'flag':'🇮🇳'
        },


        {
            'code':'hi',
            'name':'Hindi',
            'flag':'🇮🇳'
        },


        {
            'code':'es',
            'name':'Spanish',
            'flag':'🇪🇸'
        },


        {
            'code':'fr',
            'name':'French',
            'flag':'🇫🇷'
        },


        {
            'code':'de',
            'name':'German',
            'flag':'🇩🇪'
        },


        {
            'code':'it',
            'name':'Italian',
            'flag':'🇮🇹'
        },


        {
            'code':'pt',
            'name':'Portuguese',
            'flag':'🇵🇹'
        },


        {
            'code':'ru',
            'name':'Russian',
            'flag':'🇷🇺'
        },


        {
            'code':'ja',
            'name':'Japanese',
            'flag':'🇯🇵'
        },


        {
            'code':'ko',
            'name':'Korean',
            'flag':'🇰🇷'
        },


        {
            'code':'zh-CN',
            'name':'Chinese',
            'flag':'🇨🇳'
        },


        {
            'code':'ar',
            'name':'Arabic',
            'flag':'🇸🇦'
        }

    ]



    @classmethod
    def validate(cls):


        if (
            cls.API_TYPE == 'google'
            and not cls.GOOGLE_API_KEY
        ):

            raise ValueError(
                "GOOGLE_API_KEY required for Google API"
            )


        return True