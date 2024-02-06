from app.helpers import build_tailwind, write_file


def test_write_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    text = "<h1>Example Domain</h1>"

    write_file(text, file_path)

    assert file_path.exists()
    assert text in file_path.read_text()


def test_build_tailwind(tmp_path):
    input_path = tmp_path / "input.css"
    output_path = tmp_path / "output.css"

    input_text = """
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    """
    output_text = "tailwindcss"

    input_path.write_text(input_text)

    build_tailwind(input_path, output_path)

    assert output_path.exists()
    assert output_text in output_path.read_text()
