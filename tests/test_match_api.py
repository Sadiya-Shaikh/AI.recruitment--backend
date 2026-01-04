from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)


def create_dummy_pdf(text=""):
    pdf_content = f"""%PDF-1.4
1 0 obj
<< /Type /Catalog >>
endobj
xref
0 1
0000000000 65535 f
trailer
<< /Root 1 0 R >>
%%EOF
{text}
""".encode()

    return io.BytesIO(pdf_content)



def test_match_fails_for_unreadable_pdf():
    response = client.post(
        "/match",
        files={
            "resume": ("resume.pdf", create_dummy_pdf(), "application/pdf")
        },
        data={
            "jd": "Looking for a Python developer with FastAPI and AWS experience"
        }
    )

    assert response.status_code == 422
    body = response.json()
    assert body["detail"] == "No readable text found in resume"



def test_empty_jd():
    response = client.post(
        "/match",
        files={
            "resume": ("resume.pdf", create_dummy_pdf(""), "application/pdf")
        },
        data={
            "jd": ""
        }
    )

    assert response.status_code == 422


def test_non_pdf_resume():
    response = client.post(
        "/match/",
        files={
            "resume": ("resume.txt", b"not a pdf", "text/plain")
        },
        data={
            "jd": "Python developer"
        }
    )

    assert response.status_code == 400
