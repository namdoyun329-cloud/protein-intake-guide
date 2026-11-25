<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>적정 단백질 섭취량 가이드</title>
  <style>
    body {
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
      max-width: 600px;
      margin: 40px auto;
      padding: 20px;
      line-height: 1.6;
      color: #333;
    }
    .input-box {
      background: #f8f9fa;
      padding: 20px;
      border-radius: 8px;
      border: 1px solid #e9ecef;
      display: flex;
      gap: 10px;
      align-items: center;
    }
    input[type="number"] {
      padding: 8px 12px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 120px;
    }
    button {
      padding: 9px 18px;
      font-size: 16px;
      background-color: #2b8a3e;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #237032;
    }
    #result-area {
      margin-top: 24px;
      display: none;
    }
    .protein-text {
      font-size: 20px;
      font-weight: bold;
      color: #2b8a3e;
      margin-bottom: 16px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
    th, td {
      border: 1px solid #dee2e6;
      padding: 12px;
      text-align: left;
    }
    th {
      background-color: #f1f3f5;
    }
  </style>
</head>
<body>

  <h2>단백질 섭취량 및 추천 식품 가이드</h2>

  <div class="input-box">
    <label for="weight-input"><strong>몸무게 입력: </strong></label>
    <input type="number" id="weight-input" placeholder="예: 65" min="1" step="0.1">
    <span>kg</span>
    <button id="analyze-btn">분석하기</button>
  </div>

  <div id="result-area">
    <p id="protein-output" class="protein-text"></p>
    <table>
      <thead>
        <tr>
          <th>추천 식품</th>
          <th>100g당 단백질</th>
          <th>추천 정도</th>
        </tr>
      </thead>
      <tbody id="food-table-body"></tbody>
    </table>
  </div>

  <script>
    const foodListsByRange = {
      low: [
        { name: "삶은 달걀", protein: "13g", level: "매우 추천 ★★★" },
        { name: "그릭 요거트", protein: "10g", level: "추천 ★★☆" },
        { name: "두부", protein: "8g", level: "보통 ★☆☆" }
      ],
      medium: [
        { name: "닭가슴살", protein: "23g", level: "매우 추천 ★★★" },
        { name: "연어", protein: "20g", level: "추천 ★★☆" },
        { name: "렌틸콩", protein: "9g", level: "보통 ★☆☆" }
      ],
      high: [
        { name: "소고기 우둔살", protein: "22g", level: "매우 추천 ★★★" },
        { name: "닭가슴살", protein: "23g", level: "매우 추천 ★★★" },
        { name: "참치(살코기)", protein: "25g", level: "추천 ★★☆" }
      ]
    };

    function getProteinGuide(weight) {
      let recommendedProtein = 0;
      let selectedFoods = [];
      let rangeDescription = "";

      if (weight < 60) {
        recommendedProtein = Math.round(weight * 1.0);
        selectedFoods = foodListsByRange.low;
        rangeDescription = "가벼운 활동 및 기초 유지 구간";
      } else if (weight >= 60 && weight < 80) {
        recommendedProtein = Math.round(weight * 1.2);
        selectedFoods = foodListsByRange.medium;
        rangeDescription = "표준 체중 및 일반 활동 구간";
      } else {
        recommendedProtein = Math.round(weight * 1.4);
        selectedFoods = foodListsByRange.high;
        rangeDescription = "고중량 및 근력 유지 집중 구간";
      }

      return {
        proteinAmount: recommendedProtein,
        foods: selectedFoods,
        recommendationSummary: rangeDescription
      };
    }

    function createTableData(foodList) {
      const tableRows = [];

      for (let i = 0; i < foodList.length; i++) {
        const item = foodList[i];
        const rowHtml = `
          <tr>
            <td>${item.name}</td>
            <td>${item.protein}</td>
            <td>${item.level}</td>
          </tr>
        `;
        tableRows.push(rowHtml);
      }

      return tableRows;
    }

    const analyzeBtn = document.getElementById("analyze-btn");
    const weightInput = document.getElementById("weight-input");
    const resultArea = document.getElementById("result-area");
    const proteinOutput = document.getElementById("protein-output");
    const foodTableBody = document.getElementById("food-table-body");

    analyzeBtn.addEventListener("click", function () {
      const weight = parseFloat(weightInput.value);

      if (isNaN(weight) || weight <= 0) {
        alert("올바른 몸무게를 입력해 주세요.");
        return;
      }

      const guideResult = getProteinGuide(weight);
      proteinOutput.textContent =
