<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>적정 단백질 섭취량 가이드</title>
  <style>
    body { font-family: 'Malgun Gothic', sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
    .input-box { margin-bottom: 20px; }
    input { padding: 8px; font-size: 16px; width: 120px; }
    button { padding: 8px 16px; font-size: 16px; cursor: pointer; background-color: #2c7be5; color: white; border: none; border-radius: 4px; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
    th { background-color: #f4f6f9; }
    .result-text { font-size: 18px; font-weight: bold; color: #333; margin-top: 20px; }
  </style>
</head>
<body>

  <h2>적정 단백질 섭취량 및 추천 식품 가이드</h2>
  
  <div class="input-box">
    <label for="weightInput">몸무게 (kg): </label>
    <input type="number" id="weightInput" placeholder="예: 65" min="1">
    <button onclick="renderGuide()">결과 보기</button>
  </div>

  <div id="intakeResult" class="result-text"></div>
  <div id="tableContainer"></div>

  <script>
    // 1. 몸무게별 추천 식품 목록 리스트 (데이터 정의)
    const foodDatabase = {
      light: [ // 60kg 미만
        { name: "계란 (2개)", protein: "12g", level: "적극 추천" },
        { name: "그릭 요거트 (100g)", protein: "10g", level: "추천" },
        { name: "두부 (반 모)", protein: "12g", level: "보통" }
      ],
      medium: [ // 60kg 이상 ~ 80kg 미만
        { name: "닭가슴살 (100g)", protein: "23g", level: "적극 추천" },
        { name: "연어 스테이크 (100g)", protein: "20g", level: "추천" },
        { name: "단백질 쉐이크 (1스쿱)", protein: "24g", level: "보통" }
      ],
      heavy: [ // 80kg 이상
        { name: "소고기 우둔살 (150g)", protein: "33g", level: "적극 추천" },
        { name: "닭가슴살 (150g)", protein: "35g", level: "적극 추천" },
        { name: "참치캔 라이트 (1캔)", protein: "25g", level: "추천" }
      ]
    };

    // 2. 몸무게를 매개변수로 받아 적정 섭취량, 추천 식품 목록, 추천 정도를 리턴하는 함수
    function getProteinGuide(weight) {
      let minIntake = 0;
      let maxIntake = 0;
      let recommendedFoods = [];

      // 몸무게 별 구간 나누기
      if (weight < 60) {
        // 체중 1kg당 0.8g ~ 1.0g 기준
        minIntake = Math.round(weight * 0.8);
        maxIntake = Math.round(weight * 1.0);
        recommendedFoods = foodDatabase.light;
      } else if (weight >= 60 && weight < 80) {
        // 체중 1kg당 1.0g ~ 1.2g 기준
        minIntake = Math.round(weight * 1.0);
        maxIntake = Math.round(weight * 1.2);
        recommendedFoods = foodDatabase.medium;
      } else {
        // 체중 1kg당 1.2g ~ 1.5g 기준
        minIntake = Math.round(weight * 1.2);
        maxIntake = Math.round(weight * 1.5);
        recommendedFoods = foodDatabase.heavy;
      }

      // 추천 식품 목록과 추천 정도(각 객체의 level 속성 포함) 및 섭취량 반환
      return {
        intakeRange: `${minIntake}g ~ ${maxIntake}g`,
        foods: recommendedFoods
      };
    }

    // 3. 'for' 문을 순회하여 표 생성용 데이터로 변환하는 함수
    function convertToTableData(foodList) {
      const tableRows = [];

      for (let i = 0; i < foodList.length; i++) {
        const item = foodList[i];
        // 표의 각 행(Row)에 들어갈 데이터 객체 형태로 가공
        tableRows.push({
          no: i + 1,
          foodName: item.name,
          proteinAmount: item.protein,
          recommendationLevel: item.level
        });
      }

      return tableRows;
    }

    // 4. 화면에 결과를 출력하는 실행 함수
    function renderGuide() {
      const weight = Number(document.getElementById("weightInput").value);
      
      if (!weight || weight <= 0) {
        alert("올바른 몸무게를 입력해 주세요.");
        return;
      }

      // 함수 호출
      const guideData = getProteinGuide(weight);
      const tableData = convertToTableData(guideData.foods);

      // 적정 단백질 섭취량 출력
      document.getElementById("intakeResult").innerText = 
        `몸무게 ${weight}kg 기준 일일 적정 단백질 섭취량: ${guideData.intakeRange}`;

      // 변환된 표 데이터로 HTML 테이블 생성
      let tableHTML = `
        <table>
          <thead>
            <tr>
              <th>번호</th>
              <th>추천 식품</th>
              <th>단백질 함량</th>
              <th>추천 정도</th>
            </tr>
          </thead>
          <tbody>
      `;

      for (let i = 0; i < tableData.length; i++) {
        tableHTML += `
          <tr>
            <td>${tableData[i].no}</td>
            <td>${tableData[i].foodName}</td>
            <td>${tableData[i].proteinAmount}</td>
            <td><strong>${tableData[i].recommendationLevel}</strong></td>
          </tr>
        `;
      }

      tableHTML += `</tbody></table>`;
      document.getElementById("tableContainer").innerHTML = tableHTML;
    }
  </script>

</body>
</html>
