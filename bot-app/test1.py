def list_languages_with_target(target):
        """Lists all available languages and localizes them to the target language.

            Target must be an ISO 639-1 language code.
                See https://g.co/cloud/translate/v2/translate-reference#supported_languages
                    """
                        translate_client = translate.Client()

                            results = translate_client.get_languages(target_language=target)

                                for language in results:
                                            print(u'{name} ({language})'.format(**language))
