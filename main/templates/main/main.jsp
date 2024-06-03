{% extends 'layout.html' %}

{% block category-content %}
<style>
    .my_category {
        padding: 5em 0em;
        margin: 1em;
        min-width: 10em;
    }
</style>
<form id="frmCategory" name="frmCategory">
    <div class="row-cols-lg-5" style="text-align: center">
        <button type="button" class="btn btn-outline-secondary my_category">Cafe</button>
        <button type="button" class="btn btn-outline-secondary my_category">Restaurant</button>
        <button type="button" class="btn btn-outline-secondary my_category">Tour</button>
        <button type="button" class="btn btn-outline-secondary my_category">Category More...</button>
    </div>
    <form id="frmCategoryMore" name="frmCategoryMore">
        <div class="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalToggleLabel">Modal 1</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row-cols-lg-2" style="text-align: center">
                            <button type="button" class="btn btn-outline-secondary my_category" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal">Ocean</button>
                            <button type="button" class="btn btn-outline-secondary my_category" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal">Mountain</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">Modal 2</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row-cols-lg-2" style="text-align: center">
                            <button type="button" class="btn btn-outline-secondary my_category" data-bs-target="#toggleData" data-bs-toggle="modal">Dynamic</button>
                            <button type="button" class="btn btn-outline-secondary my_category" data-bs-target="#toggleData" data-bs-toggle="modal">Static</button>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-outline-secondary" data-bs-target="#exampleModalToggle" data-bs-toggle="modal">Back</button>
                    </div>
                </div>
            </div>
        </div>
    </form>
    <div class="d-grid gap-2 col-6 mx-auto">
        <input type="hidden" name="" data-bs-target="#toggleData" data-bs-toggle="modal">
        <button class="btn btn-outline-secondary" data-bs-target="#exampleModalToggle" data-bs-toggle="modal">Select Advanced</button>
    </div>
</form>
{% endblock %}

{% block post-content %}
<style>
    .row {
        justify-content: center;
    }

    .card {
        max-width: 60em;
    }
</style>
<form id="frmPost" name="frmPost">
    <div class="row row-cols-1 row-cols-md-1 g-4">
        {% for i in numbers %}
        <div class="card">
            <div id="carouselExampleFade_{{ i }}" class="carousel slide carousel-fade">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://mblogthumb-phinf.pstatic.net/MjAyMDAzMTJfMzAg/MDAxNTg0MDAzODA0Njk4.NS7-m_ME1WT1ifx5YWh2J0BNKJd0ySjzilgGVc-H48Yg.ak00BOTaU0foSw5GfMkznYnX5mq17QJMeL4jTjxOlB8g.JPEG.korailblog/35.jpg?type=w800" class="d-block w-100" style="max-height: 30rem" alt="..." />
                        <div class="carousel-caption d-none d-md-block">
                            <h5>대전역</h5>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://wimg.mk.co.kr/meet/neds/2022/08/image_readtop_2022_736640_16609599085142221.jpeg" class="d-block w-100" style="max-height: 30rem" alt="..." />
                        <div class="carousel-caption d-none d-md-block">
                            <h5>성심당</h5>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://img0.yna.co.kr/photo/yna/YH/2013/09/04/PYH2013090414670006300_P2.jpg" class="d-block w-100" style="max-height: 30rem" alt="..." />
                        <div class="carousel-caption d-none d-md-block">
                            <h5>스카이로드</h5>
                        </div>
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade_{{ i }}" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade_{{ i }}" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
            <div class="card-body">
                <h5 class="card-title">
                    빵 투어~~~
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16" style="float: right">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.09.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15" />
                    </svg>
                </h5>
                <p class="card-text">구석구석 빵 맛집 찾아다...</p>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">대전역</li>
                    <li class="list-group-item">성심당</li>
                    <li class="list-group-item">스카이로드</li>
                    <li class="list-group-item">
                        <a href="#" class="card-link">더 보기</a>
                    </li>
                </ul>
                <p class="d-inline-flex gap-1" style="width: 100%; justify-content: right">
                    <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample_{{ i }}" role="button" aria-expanded="false" aria-controls="collapseExample_{{ i }}"> 댓글 </a>
                </p>
                <div class="collapse" id="collapseExample_{{ i }}">
                    <div class="card card-body">
                        <p class="card-text">
                            재밌었나용?
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16" style="float: right">
                                <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.09.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15" />
                            </svg>
                        </p>
                    </div>
                    <div class="card card-body">
                        <p class="card-text">
                            별로일듯!
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16" style="float: right">
                                <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.09.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15" />
                            </svg>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</form>
{% endblock %}