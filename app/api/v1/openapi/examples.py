from pydantic import BaseModel, JsonValue


class OpenApiExample:
    def __init__(self, model: type[BaseModel]):
        self.model = model
        self.examples: list[JsonValue] = []
        self.model.model_config["json_schema_extra"]["examples"] = self.examples  # type: ignore[index]


    def example(self, example_dict: dict) -> "OpenApiExample":
        self.examples.append(self.model(**example_dict).model_dump())
        return self


class BoxCreateRequestExample(OpenApiExample):
    def default(self):
        return self.example(
            {
                "name": "Box Shopping Norte Sul",
            }
        )


class BoxCreateResponseExample(OpenApiExample):
    def default(self):
        return self.example(
            {
                "name": "Box Shopping Norte Sul",
            }
        )
