{% extends "base.html" %}
{% block content %}
  <h2>Мини-блог</h2>
  <h3>Задание 4. Список статей (данные из SQLite)</h3>
  
  <ul class="posts-list" style="line-height: 1.8;">
    {% for post in posts %}
      <li>
        <a href="{{ url_for('post_detail', id=post.id) }}" style="font-size: 1.1em; text-decoration: none; color: #2c3e50; font-weight: bold;">
          {{ post.title }}
        </a>
        <span style="color: #7f8c8d; font-size: 0.9em;">(Просмотров: {{ post.views }})</span>
      </li>
    {% endfor %}
  </ul>
{% endblock %}