# backend/routers/jobs.py
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다
MOCK_JOBS = [
    {
        "id": 1,
        "company": "네이버",
        "title": "데이터 분석가",
        "required_skills": ["Python", "SQL", "Pandas"],
        "preferred_skills": ["Tableau", "Git"],
        "description": "서비스 이용 데이터를 분석하여 사용자 행동을 파악하고 인사이트를 도출합니다. 다양한 부서와 협업하여 데이터 기반 의사결정을 지원하고 분석 리포트를 작성합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 2,
        "company": "카카오",
        "title": "데이터 분석",
        "required_skills": ["Python", "SQL", "통계분석"],
        "preferred_skills": ["Power BI", "Machine Learning"],
        "description": "대용량 데이터를 분석하여 서비스 성과를 측정하고 개선 방향을 제안합니다. A/B 테스트 결과를 분석하고 데이터 시각화를 통해 이해관계자에게 결과를 공유합니다.",
        "deadline": "2026-08-31"
    },
    {
        "id": 3,
        "company": "LG CNS",
        "title": "데이터 분석가",
        "required_skills": ["Python", "SQL", "Excel"],
        "preferred_skills": ["R", "Tableau"],
        "description": "고객사의 데이터를 분석하여 비즈니스 문제 해결을 위한 인사이트를 제공합니다. 데이터 전처리, 통계 분석, 시각화 업무를 수행하며 프로젝트 보고서를 작성합니다.",
        "deadline": "2026-08-31"
    }
]

@router.get("/jobs", tags=["Jobs"])
def get_jobs():
    """
    취업 공고 목록을 반환하는 엔드포인트.
    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.
    """
    return {
        "count": len(MOCK_JOBS),
        "jobs": MOCK_JOBS
    }

@router.get("/jobs/{job_id}", tags=["Jobs"])
def get_job_by_id(job_id: int):
    """
    특정 공고의 상세 정보를 반환한다.
    """
    for job in MOCK_JOBS:
        if job["id"] == job_id:
            return job
            
    # 찾지 못한 경우
    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")